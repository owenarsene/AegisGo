from quart import Quart, send_file, render_template
import asyncpg
import io
import re

## 数据库连接参数
CONNECTION = {"host": "YOUR-HOST-NAME-OR-IP", "port": PORT_NO, "database": "DATABASE_NAME",
              "user": "USER_NAME", "password": "PASSWORD"}

## 目标表名/字段/ID
TABLE = "h3_count_lev13"
H3_COL = "h3_lev13"
H3_GEOM_COL = "geometry"
AGG_VAL_COL = "count"
COL_SRID = 4326

app = Quart(__name__, template_folder='./')


@app.before_serving
async def create_db_pool():
    app.db_pool = await asyncpg.create_pool(**CONNECTION)


@app.after_serving
async def close_db_pool():
    await app.db_pool.close()


@app.route("/")
async def home():
    sql = f'''
    SELECT ST_Extent(ST_Transform(ST_Envelope({H3_GEOM_COL}), 4326))
    FROM {TABLE};
    '''
    async with app.db_pool.acquire() as connection:
        box = await connection.fetchval(sql)
        box = re.findall('BOX\((.*?) (.*?),(.*?) (.*?)\)', box)[0]
        min_x, min_y, max_x, max_y = list(map(float, box))
        bounds = [[min_x, min_y], [max_x, max_y]]
        center = [(min_x + max_x) / 2, (min_y + max_y) / 2]
        return await render_template('./index.html', center=str(center), bounds=str(bounds))


@app.route("/h3_mvt/<int:z>/<int:x>/<int:y>")
async def h3_mvt(z, x, y):
    sql = f'''
    SELECT ST_AsMVT(tile.*)
    FROM
      (SELECT ST_AsMVTGeom({H3_COL}, ST_Transform(ST_TileEnvelope($1,$2,$3),{COL_SRID}), 4096, 512, true) geometry,
       {AGG_VAL_COL} count
      FROM {TABLE}
      WHERE ({H3_COL} && ST_Transform(ST_TileEnvelope($1,$2,$3),{COL_SRID}))) tile'''
    async with app.db_pool.acquire() as connection:
        tile = await connection.fetchval(sql, z, x, y)
        return await send_file(io.BytesIO(tile), mimetype='application/vnd.mapbox-vector-tile')

if __name__ == "__main__":
    app.run(port=5100)
