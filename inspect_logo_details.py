from PIL import Image

# Let's see what ig_profile_logo looks like
im = Image.open('ig_profile_logo.jpg')
print("IG logo dimensions:", im.size)
# print color histogram / colors
colors = im.getcolors(maxcolors=256)
print("Unique colors:", len(colors) if colors else ">256")

# Let's also check if there is an image in canva_og_preview
im_canva = Image.open('canva_og_preview.jpg')
print("Canva preview dimensions:", im_canva.size)
