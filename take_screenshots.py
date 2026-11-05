import os
from playwright.sync_api import sync_playwright

os.makedirs('screenshots', exist_ok=True)

targets = [
    {
        "name": "reformas_pc",
        "url": "http://localhost:3000/",
        "viewport": {"width": 1440, "height": 900},
        "is_mobile": False
    },
    {
        "name": "reformas_mobile",
        "url": "http://localhost:3000/",
        "viewport": {"width": 390, "height": 844},
        "is_mobile": True
    },
    {
        "name": "ventanas_pc",
        "url": "http://localhost:3001/",
        "viewport": {"width": 1440, "height": 900},
        "is_mobile": False
    },
    {
        "name": "ventanas_mobile",
        "url": "http://localhost:3001/",
        "viewport": {"width": 390, "height": 844},
        "is_mobile": True
    }
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    for t in targets:
        context = browser.new_context(
            viewport=t["viewport"],
            is_mobile=t["is_mobile"],
            device_scale_factor=2
        )
        page = context.new_page()
        print(f"Capturing {t['name']} from {t['url']}...")
        page.goto(t["url"], wait_until="networkidle")
        page.wait_for_timeout(1000) # wait for animations/images

        # Capture viewport / above-the-fold
        viewport_path = f"screenshots/{t['name']}_hero.png"
        page.screenshot(path=viewport_path)
        print(f"  -> Saved {viewport_path}")

        # Capture full page
        full_path = f"screenshots/{t['name']}_full.png"
        page.screenshot(path=full_path, full_page=True)
        print(f"  -> Saved {full_path}")
        
        context.close()
    browser.close()

print("All screenshots captured successfully!")
