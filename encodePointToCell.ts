import { latLngToCell, isValidCell } from "h3-js";

export interface EncodePointToCellInput {
  lat: number;
  lng: number;
  resolution: number;
}

export function encodePointToCell({
  lat,
  lng,
  resolution,
}: EncodePointToCellInput): string {
  if (!Number.isFinite(lat) || lat < -90 || lat > 90) {
    throw new Error(`Invalid latitude: ${lat}. Latitude must be between -90 and 90.`);
  }

  if (!Number.isFinite(lng) || lng < -180 || lng > 180) {
    throw new Error(`Invalid longitude: ${lng}. Longitude must be between -180 and 180.`);
  }

  if (!Number.isInteger(resolution) || resolution < 0 || resolution > 15) {
    throw new Error(
      `Invalid resolution: ${resolution}. H3 resolution must be an integer between 0 and 15.`
    ); 
  }

  const cell = latLngToCell(lat, lng, resolution);

  if (!isValidCell(cell)) {
    throw new Error("Failed to generate a valid H3 cell.");
  }
  
  return cell;
}
