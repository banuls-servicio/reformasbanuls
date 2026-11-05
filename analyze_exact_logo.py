from PIL import Image

im = Image.open('ig_profile_logo.jpg')
print("Image size:", im.size)

# Let's save a clean zoomed crop of the logo
# find bounding box of dark pixels
im_gray = im.convert('L')
bbox = None
dark_pixels = []
for y in range(im.height):
    for x in range(im.width):
        if im_gray.getpixel((x, y)) < 180:
            dark_pixels.append((x, y))

if dark_pixels:
    min_x = min(p[0] for p in dark_pixels)
    max_x = max(p[0] for p in dark_pixels)
    min_y = min(p[1] for p in dark_pixels)
    max_y = max(p[1] for p in dark_pixels)
    print(f"Bounding box: x=({min_x}, {max_x}), y=({min_y}, {max_y})")
    cropped = im.crop((min_x - 5, min_y - 5, max_x + 5, max_y + 5))
    cropped.save('banuls_official_logo.png')
    print("Saved banuls_official_logo.png")

    # Let's print detailed ASCII of the cropped logo
    sm = cropped.resize((80, 24)).convert('L')
    for y in range(sm.height):
        line = ''.join(' #'[1 if sm.getpixel((x, y)) < 150 else 0] for x in range(sm.width))
        print(line)
