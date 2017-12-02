import requests
import re
from binascii import hexlify
url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'

auth = ('butter', 'fly')

start = 1152983631
end = 2123456788
# while start < 2123456789:
#     headers = {'Range': 'bytes={0}-'.format(start)}
#     auth = ('butter', 'fly')
#     r = requests.get(url, headers=headers, auth=auth)
#     header = r.headers
#     con_range = header.get('Content-Range')
#
#     print('Content-Range:', con_range)
#     print('content-size: ', len(r.content))
#
#     if con_range:
#         start = int(re.search(r'-(\d+)/', con_range).group(1))
#         if len(r.content) < 100:
#             print('content: ', str(r.content))
#         else:
#             break
#     else:
#         start += 1
# while end > 0:
#     start = end - 1
#     headers = {'Range': 'bytes={0}-{1}'.format(start, end)}
#     auth = ('butter', 'fly')
#     r = requests.get(url, headers=headers, auth=auth)
#     header = r.headers
#     con_range = header.get('Content-Range')
#
#     print('Content-Range:', con_range)
#
#     if con_range:
#         end = int(re.search(r'(\d+)-', con_range).group(1))
#         if len(r.content) < 100:
#             print('content-size: ', len(r.content))
#             print('content: ', str(r.content))
#         else:
#             break
#     else:
#         end -= 1

# text1 = 'esrever ni emankcin wen ruoy si drowssap eht'
# the password is your new nickname in reverse
# text2 = 'and it is hiding at 1152983631'
# print(text1[::-1])

headers = {'Range': 'bytes={0}-'.format(start)}
auth = ('butter', 'fly')
r = requests.get(url, headers=headers, auth=auth)
header = r.headers
con_range = header.get('Content-Range')

print('Content-Range:', con_range)
print('content-size: ', len(r.content))

if con_range:
    open('data.dat', 'wb').write(r.content)





