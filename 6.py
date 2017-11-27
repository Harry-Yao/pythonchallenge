import zipfile
__author__ = 'harry yao'
__date__ = '2017/11/27 15:14'

z = zipfile.ZipFile("channel.zip", 'r')
next = "90052.txt"

num = 1
comments = []

while True:
    info = z.read(next)
    comments.append(z.getinfo(next).comment)
    next = info.decode('utf-8').split()[-1] + ".txt"
    if next == "comments..txt":
        print(info.decode('utf-8'))
        break

end = ""
for list in comments:
    # print(list)
    end += str(list, encoding="utf-8")
    #输出comment
print(end)


