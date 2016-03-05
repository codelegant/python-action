import gzip
import urllib.request


def deGizp(data):
    try:
        print('正在解压......')
        data = gzip.decompress(data)
        print('解压完成')
    except:
        print('未经压缩，无需解压')
    return data


urlRes = urllib.request.urlopen('http://www.zhihu.com')
data = urlRes.read().decode('UTF-8')
deGizpData = deGizp(data)
print(deGizpData)
