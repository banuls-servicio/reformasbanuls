import json, re

with open('canva_site.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'window\[\'bootstrap\'\]\s*=\s*JSON\.parse\(\'({.*?})\'\);', text)
raw_json = m.group(1).encode('utf-8').decode('unicode_escape')

# Search for "BAÑULS" in raw_json and get 300 chars around it
for m in re.finditer(r'BAÑULS|Bañuls|Ventanas|Reformas', raw_json):
    start = max(0, m.start() - 150)
    end = min(len(raw_json), m.end() + 150)
    print("CANVA OCCURRENCE:")
    print(raw_json[start:end])
    print("="*40)
