import urllib
import urllib.request

data = {}
data['word'] = 'jecvay Notes'
urlValues = urllib.parse.urlencode(data)
url = 'http://www.baidu.com/s?'
fullUrl = url + urlValues

data = urllib.request.urlopen(fullUrl).read()
data = data.decode('UTF-8')
print(data)
