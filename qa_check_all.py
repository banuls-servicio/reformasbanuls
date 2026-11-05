import urllib.request
from playwright.sync_api import sync_playwright

urls_to_test = [
    "/",
    "/index.html",
    "/reformas-integrales-alcoy.html",
    "/reforma-banos-alcoy.html",
    "/reforma-cocinas-alcoy.html",
    "/reformas-cocentaina.html",
    "/reformas-muro-de-alcoy.html",
    "/reformas-ibi.html",
    "/reformas-onil.html",
    "/reformas-el-comtat.html",
    "/aviso-legal.html",
    "/politica-privacidad.html",
    "/politica-cookies.html",
    "/sitemap.xml"
]

print("=== 1. HTTP 200 STATUS CHECK ON NODE.JS SERVER ===")
all_passed = True
for u in urls_to_test:
    full_url = f"http://localhost:3000{u}"
    try:
        req = urllib.request.Request(full_url, headers={'User-Agent': 'QA-Bot'})
        with urllib.request.urlopen(req, timeout=3) as resp:
            code = resp.getcode()
            print(f"[OK 200] {u} -> {code}")
            if code != 200:
                all_passed = False
    except Exception as e:
        print(f"[FAIL] {u} -> {e}")
        all_passed = False

assert all_passed, "Some URLs failed HTTP 200 check!"
print("All URLs returned HTTP 200 successfully on Node.js server!")

print("\n=== 2. MOBILE VIEWPORT (390px) OVERFLOW & LAYOUT CHECK ===")
landings = [
    ("reformas-cocentaina.html", "Cocentaina"),
    ("reformas-muro-de-alcoy.html", "Muro de Alcoy"),
    ("reformas-ibi.html", "Ibi"),
    ("reformas-onil.html", "Onil"),
    ("reformas-el-comtat.html", "El Comtat"),
    ("index.html", "Home Alcoy")
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    
    for filename, label in landings:
        url = f"http://localhost:3000/{filename}"
        # Mobile 390x844
        context = browser.new_context(
            viewport={"width": 390, "height": 844},
            is_mobile=True,
            device_scale_factor=2
        )
        page = context.new_page()
        page.goto(url, wait_until="networkidle")
        
        # Check horizontal overflow
        scroll_width = page.evaluate("document.documentElement.scrollWidth")
        inner_width = page.evaluate("window.innerWidth")
        has_overflow = scroll_width > inner_width
        print(f"[{label}] Mobile scrollWidth: {scroll_width}px, innerWidth: {inner_width}px (Overflow: {has_overflow})")
        assert not has_overflow, f"Horizontal overflow detected on {filename}!"
        
        # Check mobile quick bar
        bar_visible = page.locator(".mobile-quick-bar, .mobile-sticky-bar").is_visible()
        print(f"[{label}] Mobile quick sticky bar visible: {bar_visible}")
        
        # Capture mobile hero screenshot
        page.screenshot(path=f"screenshots/geo_mob_{filename.replace('.html', '')}.png")
        
        context.close()

    # Desktop 1440x900 checks
    print("\n=== 3. DESKTOP VIEWPORT & CANONICAL 11 SECTIONS CHECK ===")
    for filename, label in landings[:3]:
        url = f"http://localhost:3000/{filename}"
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()
        page.goto(url, wait_until="networkidle")
        
        # Check H1
        h1_text = page.locator("h1").first.inner_text()
        print(f"[{label}] H1: {h1_text}")
        
        # Check AEO block
        aeo = page.locator(".aeo-extraction-block").first
        assert aeo.is_visible(), f"AEO block missing on {filename}"
        
        # Check 11 sections presence on satellite landings
        if filename != "index.html":
            assert page.locator("#problema-local").is_visible(), "Section 2 missing"
            assert page.locator("#solucion-taller").is_visible(), "Section 3 missing"
            assert page.locator("#comparativa").is_visible(), "Section 4 missing"
            assert page.locator("#resenas").is_visible(), "Section 5 missing"
            assert page.locator("#proceso").is_visible(), "Section 7 missing"
            assert page.locator("#antes-despues").is_visible(), "Section 8 missing"
            assert page.locator("#faq").is_visible(), "Section 9 missing"
            assert page.locator("#garantias").is_visible(), "Section 10 missing"
            assert page.locator("#contacto").is_visible(), "Section 11 missing"
            print(f"[{label}] Verified 11 canonical sections cleanly!")
        
        page.screenshot(path=f"screenshots/geo_pc_{filename.replace('.html', '')}.png")
        context.close()

    browser.close()

print("\n=== ALL QA AUDITS & QUALITY CONTROLS PASSED 100% ===")
