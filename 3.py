import re

__author__ = 'harry yao'
__date__ = '2017/11/26 15:52'

url = 'http://www.pythonchallenge.com/pc/def/equality.html'

text = open("3.txt").read()
matchobj = re.findall('[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}', text)

result = ''

for i in matchobj:
    result += i[4]

print(result)

