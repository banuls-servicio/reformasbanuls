import os
from PIL import Image

for fn in sorted(os.listdir('public/assets')):
    path = os.path.join('public/assets', fn)
    if fn.endswith('.svg'):
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            c = f.read()
        print(f"SVG {fn} len={len(c)}")
        # Check text in svg
        import re
        txts = re.findall(r'<text[^>]*>(.*?)</text>', c, re.DOTALL)
        if txts:
            print(f"  Texts in {fn}: {txts}")
    elif fn.endswith(('.png', '.jpg')):
        im = Image.open(path)
        # check if it looks like a logo (e.g. small height, or transparent background, or specific aspect ratio)
        print(f"IMG {fn}: size={im.size}, mode={im.mode}")
