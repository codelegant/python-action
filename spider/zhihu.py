# coding=utf-8
import gzip
import urllib.request
import re
import http.cookiejar
import urllib.parse
import json


def get_csrf(data):
    cer = re.compile('name="_xsrf" value="([\w-]*)"', flags=0)  # 正则中有括号，匹配括号中的字符，试试用零宽断言
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


url = 'https://www.zhihu.com'
opener = my_opener()

"""获取防跨站请求伪造代码"""
getCsrf = opener.open(url)
# getCsrf=urllib.request.urlopen(url);
csrfData = de_gzip(getCsrf.read()).decode('UTF-8')
csrf = get_csrf(csrfData)  # 需要处理cookie，登录的时候需要使用
# print(csrf)
# exit()

"""登录信息传递给登录链接"""
signinUrl = url + '/login/email'
postDict = {
    'email': '***',
    'password': '***',
    '_xsrf': csrf,
    'remember_me': 'true'
}
postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(signinUrl, postData)
data = de_gzip(op.read()).decode('UTF-8')  # 如何将ASCII转换成Native?然后判断是否登录成功
"""判断登录返回信息"""
if (op.status == 200 and op.getheader('Content-Type') == 'application/json'):
    resJson = json.loads(data)
    print(resJson)
    if (resJson['r'] == 0):  # 登录成功
        success = opener.open(url)
        successData = de_gzip(success.read()).decode('UTF-8')
        print(successData)
    else:
        print('登录不成功，返回信息：' + resJson)

"""登录成功，手动获取数据"""
# success = opener.open(url)
# successData = de_gzip(success.read()).decode('UTF-8')
# print(successData)
