import xmlrpc.client
__author__ = 'harry yao'
__date__ = '2017/11/29 21:02'

client = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print(client.system.listMethods())
print(client.system.methodHelp('phone'))
print(client.phone('Bert'))
