# AurumX mockup

Static design mockup for the AurumX brand, in the same design as `tbwndemo` (dark ground, gold accent, one light interlude). Plain HTML, CSS and a little JavaScript. No build step.

| Page | What it shows |
|---|---|
| `/` | Landing page |
| `/membership/` | Partner-broker membership application (dummy) |
| `/admin/` | Demo admin: review and approve applications |
| `/access/` | Member log-in and dashboard with sample data: Signal, Chart, Stats, Planner, Account |
| `/support/`, `/terms/`, `/privacy/` | Placeholder legal and support pages |

## How the demo flow works

1. Apply on `/membership/`. The e-mail code in this demo is always `123456`.
2. Open `/admin/` and approve the application. A key like `AURX-XXXX-XXXX` is issued ("emailed" is simulated).
3. Log in on `/access/` with that key. `AURX-DEMO-2026` always works.

Applications live in the browser's `localStorage` only (key `aurumx_demo_apps_v1`), so nothing is sent or stored anywhere. Clear it with "Reset the demo data" on the admin page.

## Placeholders to replace

- Wordmark `AURUMX` in the header: replace with the real logo.
- Partner broker link and code (`AURUMX-0000`), deposit tiers ($100 / $200 / $250) and their trading-day labels.
- Record figures on the landing page are samples.
- Support e-mail `support@aurumx.example` and the wording of terms and privacy.

The Chart tab uses TradingView Lightweight Charts v5 (Apache-2.0), vendored in `assets/lightweight-charts.js`, with generated sample candles. Its TradingView attribution mark is kept on purpose.

All pages carry `noindex`. Deploy: Vercel serves the repository root as a static site.
