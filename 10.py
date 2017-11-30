import re
__author__ = 'harry yao'
__date__ = '2017/11/29 19:22'

result = '1'
# a = ['1', '11', '21', '1211', '111221', '312211']

for i in range(30):
    # 不能理解正则表达式是怎么切的
    marchobj = re.findall('((?P<w>\d)(?P=w)*)', result)
    a = map(lambda x: '%s%s' % (len(x[0]), x[1]), re.findall('((?P<w>\d)(?P=w)*)', result))
    result = ''.join(a)

print(len(result))