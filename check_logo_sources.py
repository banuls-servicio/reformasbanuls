import urllib.request
import re
import json

def check_instagram():
    req = urllib.request.Request('https://www.instagram.com/proyectos.banuls/', headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    })
    try:
        html = urllib.request.urlopen(req, timeout=8).read().decode('utf-8', errors='ignore')
        og = re.findall(r'property="og:image"\s+content="([^"]+)"', html)
        print("IG OG image:", og)
        pics = re.findall(r'https://[^"]+cdninstagram[^"]+', html)
        print("IG pics found:", len(pics), pics[:3])
    except Exception as e:
        print("IG err:", e)

def check_canva_img():
    # Let's inspect canva_img_check.png with Pillow
    from PIL import Image
    im = Image.open('canva_img_check.png')
    print("Canva OG image size:", im.size)
    # Check if we can save it as JPG or see if it has text
    im.save('canva_og_preview.jpg')

check_instagram()
check_canva_img()
