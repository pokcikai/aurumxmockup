"""Render tools/og/og-card.html to assets/og-card.png (1200x630)."""
import pathlib
from playwright.sync_api import sync_playwright
root = pathlib.Path(__file__).resolve().parents[2]
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=1)
    pg.goto((root / "tools/og/og-card.html").as_uri())
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(800)
    pg.screenshot(path=str(root / "assets/og-card.png"))
    b.close()
print("assets/og-card.png written")
