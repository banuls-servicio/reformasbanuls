from playwright.sync_api import sync_playwright

def test_site(url, name, expected_review_url):
    print(f"\n--- Testing {name} ({url}) ---")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()
        page.goto(url, wait_until="networkidle")
        
        # 1. Check Cookie Banner
        banner = page.locator("#cookie-consent-banner")
        is_banner_visible = banner.is_visible()
        print(f"Cookie banner visible initially: {is_banner_visible}")
        assert is_banner_visible, "Cookie banner should be visible for new visitor"
        
        # Click "Aceptar todas"
        accept_btn = page.locator("#btn-accept-cookies")
        accept_btn.click()
        page.wait_for_timeout(500)
        
        is_banner_hidden = not banner.is_visible()
        print(f"Cookie banner hidden after accept: {is_banner_hidden}")
        assert is_banner_hidden, "Cookie banner should hide after consent"
        
        # Check localStorage
        consent_val = page.evaluate("localStorage.getItem('banuls_cookie_consent_v2')")
        print(f"LocalStorage consent value: {consent_val}")
        assert consent_val == 'granted', "Consent should be 'granted'"

        # 2. Check Reviews link and stars
        rev_link = page.locator("a:has-text('Ver todas las reseñas'), a:has-text('Ver reseñas en Google Maps')").first
        href = rev_link.get_attribute("href")
        print(f"Review link href: {href}")
        assert expected_review_url in href, f"Expected {expected_review_url} in {href}"
        
        # Check all displayed stars are 5 stars or 4 stars
        stars_elements = page.locator(".google-review-card .google-stars").all()
        print(f"Found {len(stars_elements)} review cards")
        for idx, s in enumerate(stars_elements):
            text = s.inner_text().strip()
            # Count stars
            count_5 = text.count('\u2605')
            print(f"  Card {idx+1} has {count_5} full stars")
            assert count_5 >= 4, f"Review card {idx+1} must be 4 or 5 stars"

        # 3. Check Legal Footer Links
        aviso_link = page.locator("footer a[href='aviso-legal.html']").first
        priv_link = page.locator("footer a[href='politica-privacidad.html']").first
        cookies_link = page.locator("footer a[href='politica-cookies.html']").first
        assert aviso_link.is_visible(), "Aviso Legal link should exist in footer"
        assert priv_link.is_visible(), "Privacidad link should exist in footer"
        assert cookies_link.is_visible(), "Cookies link should exist in footer"
        print("All legal links verified in footer!")

        context.close()
        browser.close()
    print(f"--- {name} passed all checks successfully! ---")

test_site("http://localhost:3000/", "Reformas Bañuls", "share.google")
test_site("http://localhost:3001/", "Ventanas Bañuls", "google.com/maps/place/Ventanas+Ba%C3%B1uls")
print("\n[ALL SITES PASSED TEST VERIFICATION SUCCESSFULLY]")
