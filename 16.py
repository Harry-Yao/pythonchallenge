from PIL import Image
__author__ = 'harry yao'
__date__ = '2017/12/1 10:40'

im = Image.open('mozart.gif')
for y in range(im.size[1]):
    line = [im.getpixel((x, y)) for x in range(im.size[0])]
    idx = line.index(195)
    line = line[idx:] + line[:idx]
    [im.putpixel((x, y), line[x]) for x in range(len(line))]

im.show()

