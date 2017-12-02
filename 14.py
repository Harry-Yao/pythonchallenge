from PIL import Image
__author__ = 'harry yao'
__date__ = '2017/11/30 18:52'

im = Image.open('wire.png')

img = Image.new(im.mode, (100, 100))
flag = 0  
dmax = 9
dmin = 1  
x = 0  
y = 0  
for i in range(100):
    # img.putpixel((x, y), im.getpixel((i, 0)))
    if flag == 0:
        x += 1
    elif flag == 1:
        y += 1
    elif flag == 2:
        x -= 1
    else:
        y -= 1

    if dmin == dmax:
        flag += 1
        dmin = 1
        if flag == 4:
            flag = 0
            dmax -= 2
            y += 1
            x += 1
    else:
        dmin += 1

img.show()






