import pickle
__author__ = 'harry yao'
__date__ = '2017/11/27 14:56'

text = open("banner.p", "rb")

data = pickle.load(text)

str = ""
for list in data:
    print(list)
    for i in list:
        str += i[0] * i[1]
    str += '\n'
print(str)
