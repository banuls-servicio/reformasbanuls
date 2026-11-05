import urllib.request
import re

url = 'https://www.google.com/search?kgmid=/g/12qg_r_yd&hl=es-ES&q=Reformas+Ba%C3%B1uls'
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'es-ES,es;q=0.9'
})

try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print('Length:', len(html))
        
        # Look for rating
        ratings = re.findall(r'(\d[,\.]\d)\s*de\s*5|aria-label="([\d\.,]+ de 5 estrellas|\d[,\.]\d stars)', html)
        print('Ratings:', ratings[:5])

        # Look for reviews count
        reviews = re.findall(r'(\d+)\s*(?:reseñas|opiniones|reviews)', html, re.I)
        print('Reviews count:', set(reviews[:10]))

        # Look for actual review quotes / authors
        quotes = re.findall(r'class="[^"]*(?:review|comment|snippet)[^"]*"[^>]*>([^<]+)<', html, re.I)
        print('Quotes:', quotes[:5])

        # Place ID or data-pid
        pids = re.findall(r'data-pid="([^"]+)"|data-cid="([^"]+)"|0x[0-9a-f]+:0x[0-9a-f]+', html)
        print('PIDs/CIDs:', pids[:5])
        
        # Look for maps link
        maps = re.findall(r'https://(?:www\.)?google\.[a-z\.]+/maps/[^\s"\'<>]+', html)
        print('Maps links:', maps[:3])
except Exception as e:
    print('Error:', e)
