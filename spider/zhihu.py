import gzip
import urllib.request
import re


def de_gzip(data):
    try:
        print('正在解压......')
        data = gzip.decompress(data)
        print('解压完成')
    except:
        print('未经压缩，无需解压')
    return data


def get_xsrf(data):
    cer = re.compile('name="_xsrf" value="(.*)"', flags=0)  # 正则中有括号，匹配括号中的字符，试试用零宽断言
    str_list = cer.findall(data)
    return str_list[0]


urlRes = urllib.request.urlopen('http://www.zhihu.com')
originData = urlRes.read().decode('UTF-8')
deGizpData = de_gzip(originData)
xsrf = get_xsrf(deGizpData)
print(xsrf)
