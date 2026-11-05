from PIL import Image

im = Image.open('ig_profile_logo.jpg')
w, h = im.size
print("Width:", w, "Height:", h)

# Let's crop the center where the logo text is
# lines 8 to 16 in a 25-height grid means y from roughly 0.3*h to 0.7*h
cropped = im.crop((0, int(h * 0.25), w, int(h * 0.75)))
cropped.save('ig_logo_center.jpg')
print("Saved ig_logo_center.jpg")
