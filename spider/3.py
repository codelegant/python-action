# python documents\github\python\spider\3.py
import re
import urllib.request
import http.cookiejar
import urllib

from collections import deque

defaultHead = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en:1=0.6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
}


def makeMyOpener(head=defaultHead):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        ele = (key, value)
        header.append(ele)
    opener.addheaders = header
    return opener


def saveFile(data):
    save_path = 'temp.txt'
    f_obj = open(save_path, 'wb')
    f_obj.write(data)
    f_obj.close()


queue = deque()
visited = set()

url = 'http://laichuanfeng.com'

queue.append(url)
cnt = 0

oper = makeMyOpener()
while queue:
    url = queue.popleft()  # 队首元素出队
    visited |= {url}  # 标记为已访问

    print('已经抓取：' + str(cnt) + '******正在抓取 <---' + url)
    cnt += 1
    try:
        urllop = oper.open(url, timeout=30)
    except:
        print('获取页面数据超时')
        continue
    if 'html' not in urllop.getheader('Content-Type'):
        print('返回类型不是html')
        continue

    # 避免程序异常中止, 用try..catch处理异常
    try:
        data = urllop.read().decode('utf-8')
    except:
        print('转码UTF-8出现异常')
        continue
    try:
        saveFile(data)
    except:
        print('保存数据失败')

    # 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
    linkre = re.compile('href="(.+?)"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('加入队列 ----->' + x)
    if len(queue) > 100:
        break