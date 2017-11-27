from urllib import request
__author__ = 'harry yao'
__date__ = '2017/11/27 14:23'

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
response = request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')

page = response.read()
page = page.decode('utf-8')
num_list = page.split()
i = 0
while i < 400:
    req = request.Request(url+num_list[-1])
    page = request.urlopen(req).read()
    page = page.decode('utf-8')
    print(page)
    num_list = page.split()
    i += 1



