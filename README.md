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

All pages carry `noindex`. Deploy: the Vercel project is linked to this repository, so every push to `main` publishes to https://aurumxmockup.vercel.app (the repository root is served as a static site).

## Share card (Open Graph)

`assets/og-card.png` is 1200x630. Its source is `tools/og/og-card.html`; re-render it with `python tools/og/build.py` (needs Playwright and network for the Google fonts). Every page carries the Open Graph and Twitter tags. The landing page uses a 52-character title, a 133-character meta description and a 108-character `og:description`. `og:image` points at `https://aurumxmockup.vercel.app/assets/og-card.png`: when AurumX gets its own domain, change `SITE` in the page heads (search for `aurumxmockup.vercel.app`).
