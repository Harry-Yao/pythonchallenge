from PIL import Image

# python图像处理不会(T_T)
im = Image.open("cave.jpg")
x = int(im.size[0])
y = int(im.size[1])

odd = Image.new(im.mode, (x, y))
even = Image.new(im.mode, (x, y))

for x in range(1, im.size[0], 2):
    for y in range(1, im.size[1], 2):
        odd.putpixel((int((x-1)/2), int((y-1)/2)), im.getpixel((x, y)))

for x in range(1, im.size[0], 2):
    for y in range(1, im.size[1], 2):
        even.putpixel((int(x/2), int(y/2)), im.getpixel((x, y)))

even.show()
