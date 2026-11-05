from PIL import Image

im = Image.open('ig_profile_logo.jpg')
# resize to 40x40 and print ascii
im_small = im.resize((50, 25)).convert('L')
chars = " .:-=+*#%@"
for y in range(im_small.height):
    line = "".join(chars[im_small.getpixel((x, y)) * (len(chars) - 1) // 255] for x in range(im_small.width))
    print(line)
