# AegisGo

Location-aware situational awareness. Phase 1 is a **static Expo prototype** with mock incidents. There is no live backend, identity, push, or media upload.

Priority: Safety > Trust > Privacy > Usability > Speed > Monetization.

AegisGo shows nearby **reported situations**. It does not claim a place is safe or dangerous.

## Start

```bash
npm start
```

Then open Expo Go, an emulator, or `npm run web`.

## Checks

```bash
npx tsc --noEmit
npm run lint
npm test
```

Pinned for this phase (do not blindly upgrade): Expo SDK 57, React 19.2.3, React Native 0.86.3, TypeScript 6.0.x.

## Architecture (Phase 1)

- Expo Router tabs: Map, Nearby, Report, Alerts, Profile
- Domain logic in `lib/` (confidence, geo, time, PII, notification thresholds)
- Mock incidents in `data/mockIncidents.ts`
- Session state in `store/AppState.tsx` (local reports and confirmations)
- Schematic map in `features/map/MockRiskMap.tsx` (no native map SDK yet)

## Manual QA

1. Complete four onboarding screens. Location is optional and not requested with camera/contacts/background tracking.
2. Filter time on Map. Empty copy must **not** say the area is safe.
3. Open a marker/card. Impact (severity) and confidence are separate.
4. Submit a report with no description. It appears under Profile → My reports as screening / pending.
5. Confirm an incident twice: the second attempt is blocked in this session.
6. Try a phone number or “looks suspicious” in the description: submit is blocked.
7. Clear local reports from Profile.
8. Alerts list omits Tier C (map-only) items and uses calm copy.

## Limits / next phase

No auth, RLS, PostGIS queries, real moderation queue, push, evidence upload, or background location. Mock coordinates are for a schematic downtown, not a live feed.

Next: Phase 2 — Authentication + backend (Supabase, RLS, validated CRUD).
