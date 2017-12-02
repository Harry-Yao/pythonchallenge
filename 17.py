import requests
import bz2
import urllib.parse
import xmlrpc.client
__author__ = 'harry yao'
__date__ = '2017/12/1 11:16'

text = '''
info=you+should+have+followed+busynothing...; wikiticket=%18%13%E3%B5%17%05%85%2Fi%DFK%F2%2Fb%24%3Cm%BFI%D7b
Host:www.pythonchallenge.com
'''
# url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
# busynothing = 12345
# r = requests.get(url, params={'busynothing': busynothing})
# text = ''
# while True:
#     r = requests.get(url, params={'busynothing': busynothing})
#     busynothing = r.text.split()[-1]
#     info = r.cookies.get('info')
#     if info is None:
#         break
#     text += info

# info = 'BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'
# byts = urllib.parse.unquote_to_bytes(info.replace('+', '%20'))
# print(byts.__class__)
# print(bz2.decompress(byts).decode('utf-8'))
#
# client = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
# print(client.phone('Leopold'))

url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'

headers = {'Cookie': 'info=the flowers are on their way'}
r = requests.get(url, headers=headers)

print(r.text)
