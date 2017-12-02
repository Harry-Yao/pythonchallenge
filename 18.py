import difflib
from binascii import unhexlify
from PIL import Image
from io import BytesIO

f = open('delta.txt')
data = f.read()
# f.close()
# f1 = ''
# f2 = ''
# f3 = ''
# t = []
# data = data.splitlines()
# line = 1
# for i in data:
#     if line == 2197:
#         print(i)
#     left = i[:53]
#     right = i[56:]
#     diff = difflib.ndiff(left, right)
#     line += 1
#     for j in diff:
#         s = j[:1]
#         code = j[2:]
#         if code == ' ':
#             continue
#         if s == '+':
#             f1 += code
#         elif s == '-':
#             f2 += code
#         elif s == ' ':
#             f3 += code
#
# open('f1.png', 'wb').write(binascii.unhexlify(f1))
# open('f2.png', 'wb').write(binascii.unhexlify(f2))
# open('f3.png', 'wb').write(binascii.unhexlify(f3))
left = []
right = []

for line in data.splitlines():
    left.append(line[:53])
    right.append(line[56:])

f.close()

d = difflib.Differ()
result = list(d.compare(left, right))
pic1 = ''
pic2 = ''
pic3 = ''
for line in result:
    if line[0] == ' ':
        pic1 += line[1:].replace(' ', '').replace('\n', '')
    elif line[0] == '+':
        pic2 += line[1:].replace(' ', '').replace('\n', '')
    elif line[0] == '-':
        pic3 += line[1:].replace(' ', '').replace('\n', '')

Image.open(BytesIO(unhexlify(pic1))).show()
Image.open(BytesIO(unhexlify(pic2))).show()
Image.open(BytesIO(unhexlify(pic3))).show()
