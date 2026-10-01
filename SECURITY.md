# SECURITY

Phase 1 has no server. Still treat the client as hostile for future work.

- Never put service-role secrets in the mobile client.
- Validate every mutating request server-side (Phase 2+).
- Rate-limit report create, confirmations, media, signup, notification endpoints.
- Defend against spam, bots, mass reporting, coordinate spoofing, SQLi, XSS in text, malicious media, IDOR, privilege escalation.
- Row Level Security on all public tables before live data.
- Admin actions always write `audit_logs`.
- Phase 1 client blocks obvious PII and person-accusation phrases in report text. This is not a moderation engine.
