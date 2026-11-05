from playwright.sync_api import sync_playwright

url = "https://www.google.com/search?kgmid=/g/12qg_r_yd&hl=es-ES&q=Reformas+Ba%C3%B1uls"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(locale="es-ES")
    page.goto(url, wait_until="networkidle")
    # Accept cookies if prompted
    try:
        page.locator("button:has-text('Aceptar todo'), button:has-text('Acepto')").click(timeout=3000)
        page.wait_for_timeout(1000)
    except:
        pass
    
    title = page.title()
    text = page.inner_text("body")
    print("Page Title:", title)
    
    # Check for keywords
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    relevant_lines = [l for l in lines if any(k in l.lower() for k in ['reseña', 'estrella', 'opinión', 'valoraci', 'carrer', 'murillo', 'bañuls', 'reformas'])]
    print("Relevant lines sample:")
    for l in relevant_lines[:25]:
        print("  -", l)
        
    page.screenshot(path="screenshots/gbp_reformas_search.png")
    print("Screenshot saved to screenshots/gbp_reformas_search.png")
    browser.close()
