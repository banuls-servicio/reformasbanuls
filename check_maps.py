import urllib.request
import re

url = 'https://www.google.com/maps/place/Ventanas+Ba%C3%B1uls,+Carrer+Murillo,+41,+03802+Alcoi,+Alicante/data=!4m2!3m1!1s0xd61865575a2caa7:0xe262f3333a9606ab'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
try:
    html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
    print('Maps HTML len:', len(html))
    with open('maps_dump.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    # Check ratings
    matches = re.findall(r'(\d[,\.]\d)\s*estrellas|(\d[,\.]\d)\s*reseñas|\"([0-9\.]+)\",null,\[null,null,(\d+)\]', html)
    print("Rating patterns:", matches[:10])
    
    # Check photo urls
    photos = re.findall(r'https://lh[0-9]\.googleusercontent\.com/[^\s"\'>]+', html)
    print("Found Google photos:", len(set(photos)))
    for p in list(set(photos))[:5]:
        print("  -", p)
except Exception as e:
    print('Err:', e)
