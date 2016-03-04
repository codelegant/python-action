import urllib.request

url = 'http://www.baidu.com'
urlRes = urllib.request.urlopen(url)
data = urlRes.read()
data = data.decode('UTF-8')
f = open('baidu.html', 'r+')  # 如何创建一个新的文件？
f.write(repr(data))  # 如何处理换行符？
f.close()
print(data)
