import gzip
import urllib.request
import re
import http.cookiejar
import urllib.parse


def get_csrf(data):
    cer = re.compile('name="csrf" value="([\w-]*)"', flags=0)  # 正则中有括号，匹配括号中的字符，试试用零宽断言
    str_list = cer.findall(data)
    return str_list[0]


def de_gzip(data):
    try:
        print('正在解压......')
        data = gzip.decompress(data)
        print('解压完成')
    except:
        print('未经压缩，无需解压')
    return data


defaultHead = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en:1=0.6',
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded'
}


def my_opener(head=defaultHead):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        ele = (key, value)
        header.append(ele)
    opener.addheaders = header
    return opener


url = 'http://xiaolai.kiwifi.cn/account'

urlReq = urllib.request.Request(
    url,
    None,
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
        'Connection': 'keep-alive'
    })  # 初始化连接的参数
urlRes = urllib.request.urlopen(urlReq)  # 打开一个连接，获取信息
originData = urlRes.read().decode('UTF-8')
csrf = get_csrf(originData)
print(csrf)
postDict = {
    'account': 'xiaolai@kiwifi.cn',
    'password': '123456',
    'csrf': get_csrf(originData),
    'type': 'signin'
}
postData = urllib.parse.urlencode(postDict).encode()
opener = my_opener()
op = opener.open(url, postData)
data = de_gzip(op.read()).decode('UTF-8')
print(data)
