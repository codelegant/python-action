# coding=utf-8
from requests import get

from spider import selflib


# r = requests.get(
#     'https://dianying.taobao.com/showAction.json?_ksTS=1464542437987_59&jsoncallback=jsonp60&action=showAction&n_s=new&event_submit_doGetSoon=true')
# print(r.status_code)
# print(r.text)

def get_from_api():
    """通过访问api获取数据"""
    params = {'_ksTS': selflib.get_timestamp_13()}


def get_from_page():
    """通过抓取页面数据获取数据"""
    r = get('')
