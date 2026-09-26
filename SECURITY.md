# Security Policy

## Supported Versions

Only the latest state of the `dev` branch (and any `1.x` release cut
from it) receives security fixes. The `master` branch mirrors upstream
and is intentionally untouched.

| Version | Supported          |
| ------- | ------------------ |
| dev latest (`1.x`) | :white_check_mark: |
| `master` mirror / `<= 1.0.5` upstream | :x: |

## Reporting a Vulnerability

Please do **not** open a public issue. Use GitHub's private
vulnerability reporting: the repository's **Security** tab →
**Report a vulnerability**. Reports are triaged on a best-effort basis;
expect an initial response within 14 days.

## Scope Notes

- The library has **zero runtime dependencies** (stdlib only), which is
  its strongest supply-chain property — please keep it that way.
  Dependency updates cover dev tooling and CI actions only.
- The prayer-time math is deterministic and offline; the realistic
  threat model is supply-chain (compromised dev dependency or action)
  and correctness (wrong times), not remote exploitation.
