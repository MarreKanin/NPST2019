from PIL import Image


im = Image.open("30_dl.png")

print("Showing RGBA channels: ")
#img = Image.new("RGB", (n+1, n+1), (255, 255, 255))

print(im.getpixel((779, 599)))

im = im.convert("RGB")

print("Showing RGB channels: ")
print(im.getpixel((779, 599)))

im.save("transsmission-solved.png")
