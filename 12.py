from PIL import Image
__author__ = 'harry yao'
__date__ = '2017/11/29 20:28'

f = open('evil2.gfx', 'rb')
content = f.read()
f.close()

#  生成的图片打不开
for i in range(5):
    f = open('12/%d.jpg' % i, 'wb')
    f.write(content[i::5])
    f.close()
