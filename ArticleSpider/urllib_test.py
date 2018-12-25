from urllib import request

response = request.urlopen('http://www.baidu.com')
print(response.read())
