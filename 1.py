__author__ = 'harry yao'
__date__ = '2017/11/26 15:38'

a = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# my method
b = ""

for i in a:
    if 121 <= ord(i) < 123:
        i = chr(ord(i) - 24)
    elif 96 < ord(i) < 121:
        i = chr(ord(i) + 2)
    b += i

print(b)

# The author's method
str1 = 'abcdefghijklmnopqrstuvwxyz'
str2 = 'yzabcdefghijklmnopqrstuvwx'
trantab = str.maketrans(str2, str1)
print(a.translate(trantab))

c = 'map'

print(c.translate(trantab))
