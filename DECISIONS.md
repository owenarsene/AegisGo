# DECISIONS

## Phase 1 vehicle is Expo, not the prior web prototype

- **Date:** 2026-10-01
- **Context:** Master spec requires Expo + TypeScript static prototype. A previous Downloads README described a browser prototype.
- **Options:** Continue web; Expo only; web as UX lab + Expo as product.
- **Chosen:** New Expo app at `C:\Users\USER\aegisgo`.
- **Reason:** Matches the product stack and native permission/notification path.
- **Consequences:** Web README prototype is not this repo. Do not merge those codepaths without a new decision.

## Schematic map instead of react-native-maps in Phase 1

- **Date:** 2026-10-01
- **Context:** Need mock markers without extra native modules.
- **Options:** react-native-maps; Mapbox; schematic projection.
- **Chosen:** Schematic `MockRiskMap`.
- **Reason:** Runs in Expo Go and web; Phase 1 validates IA not map tiles.
- **Consequences:** Distances use haversine on mock coordinates; visual map is not street-accurate.

## Session-only local reports

- **Date:** 2026-10-01
- **Context:** Spec requires completing a report that creates a local mock.
- **Chosen:** In-memory `AppState`; cleared from Profile.
- **Consequences:** Reports vanish on reload. Persistence waits for Phase 2.

## Confidence labels, not numeric scores in UI

- **Date:** 2026-10-01
- **Chosen:** Unverified / Multiple reports / High confidence / Official / trusted source.
- **Reason:** Master spec forbids exposing a complex score or mixing severity with confidence.
