from PIL import Image
__author__ = 'harry yao'
__date__ = '2017/11/29 18:14'

img = Image.open('oxygen.png')
text = ''

i = 0
while i < img.width:
    pix = img.getpixel((i, 47))
    i += 7


text2 = "105, 110, 116, 101, 103, 114, 105, 116, 121"
for i in text2.split(','):
    print(chr(int(i)))




