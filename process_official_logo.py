from PIL import Image

im = Image.open('banuls_official_logo.png')
# Make transparent background (white -> transparent)
im_rgba = im.convert('RGBA')
datas = im_rgba.getdata()

new_data_dark = []
new_data_white = []

for item in datas:
    # item is (r, g, b, a)
    # Background is near white: r > 230, g > 230, b > 230
    brightness = (item[0] + item[1] + item[2]) / 3
    if brightness > 220:
        new_data_dark.append((255, 255, 255, 0))
        new_data_white.append((255, 255, 255, 0))
    else:
        # Dark pixel: make it crisp dark anthracite (#0F172A)
        alpha = int((1.0 - (brightness / 220.0)) * 255)
        new_data_dark.append((15, 23, 42, alpha))
        # For white version: make it pure white
        new_data_white.append((255, 255, 255, alpha))

im_rgba.putdata(new_data_dark)
# Resize 4x with bicubic for high DPI sharpness
w, h = im_rgba.size
im_hires_dark = im_rgba.resize((w * 4, h * 4), Image.Resampling.LANCZOS)
im_hires_dark.save('assets/img/logo-oficial-banuls.png')
print("Saved assets/img/logo-oficial-banuls.png (dark)")

im_rgba.putdata(new_data_white)
im_hires_white = im_rgba.resize((w * 4, h * 4), Image.Resampling.LANCZOS)
im_hires_white.save('assets/img/logo-oficial-banuls-white.png')
print("Saved assets/img/logo-oficial-banuls-white.png (white)")
