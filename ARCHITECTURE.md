# ARCHITECTURE

Phase: **1 Static prototype**. Client-only.

```
app/                 Expo Router screens
components/ui/       Design primitives and incident presentation
features/map/        Schematic risk map
store/               Session mock state
lib/                 Pure domain rules
data/                Mock incidents
types/               Shared TypeScript models
constants/           Tokens and taxonomy labels
supabase/migrations  Schema intent for later phases
tests/               Domain unit tests
docs/                Master product context excerpt pointer
```

## Runtime

React Native + Expo SDK 57 + Expo Router + TypeScript strict.

Phase 1 does **not** use react-native-maps, Supabase, or push. The map is a projected schematic so Expo Go and web both run without extra native modules.

## Later (not implemented)

PostgreSQL + PostGIS, Supabase Auth/DB/Storage, Edge Functions, RLS, TanStack Query, Zod at the API boundary, admin web for moderation.

Sensitive writes must never be trusted from the client. Service-role keys never ship in the app.

## Navigation

- `/onboarding` — 4 screens, progressive location
- `/(tabs)` — Map, Nearby, Report, Alerts, Profile
- `/incident/[id]` — detail, confirm/contradict, suggested actions
