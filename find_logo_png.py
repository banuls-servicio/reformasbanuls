import os
from PIL import Image

for fn in os.listdir('public/assets'):
    if fn.endswith('.png'):
        im = Image.open('public/assets/' + fn)
        # check if it has transparent background or high contrast text
        if im.size[0] > 700:
            # resize small to 60x20 and check if mostly white/black
            sm = im.resize((60, 20)).convert('L')
            extrema = sm.getextrema()
            print(f"{fn}: size={im.size}, extrema={extrema}")
