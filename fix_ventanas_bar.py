import glob
import re

for fpath in glob.glob(r'C:\Users\edgvi\Documents\ventanasbanuls\*.html'):
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    c = re.sub(
        r'🪟\s*Ventanas\s*&amp;\s*Aislamiento\s*\(ventanasbañuls\.com\)',
        '🪟 Ventanas Bañuls',
        c
    )
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print('Updated all ventanasbanuls HTML network bars!')
