from PIL import Image

img = Image.open("perrita.jpeg")
w, h = img.size
print(f"Size: {w}x{h}")

# Portrait photo: face is in upper-center ~50% of height
# Use full width as square base, crop top 56% as square
crop_dim = int(h * 0.56)          # ~717px → almost full width
if crop_dim > w:
    crop_dim = w                    # cap to image width

left = (w - crop_dim) // 2
top  = int(h * 0.00)              # start from very top
right  = left + crop_dim
bottom = top  + crop_dim

cropped = img.crop((left, top, right, bottom))
cropped = cropped.resize((256, 256), Image.LANCZOS)
cropped.save("favicon.jpg", "JPEG", quality=90)
print(f"Saved favicon.jpg: cropped ({left},{top},{right},{bottom}) → 256x256")
