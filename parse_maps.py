import re

with open('maps_dump.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Search for review text strings or star ratings
for m in re.finditer(r'(Ventanas Bañuls|Reformas|Carrer Murillo|Murillo, 41)', text):
    start = max(0, m.start() - 100)
    end = min(len(text), m.end() + 200)
    print("MATCH:", text[start:end])
    print("---")
    break

# Look for reviews or ratings in JS arrays
# Google Maps stores reviews like [["Author", ...], ["Review text", ...]]
reviews = re.findall(r'\[\"([A-ZÁÉÍÓÚ][^\"]{20,250})\"\]', text)
print(f"Potential text blocks: {len(reviews)}")
for r in reviews[:10]:
    if any(w in r.lower() for w in ['ventana', 'reforma', 'trabajo', 'precio', 'instalación', 'atención', 'profesional']):
        print("REVIEW CANDIDATE:", r)
