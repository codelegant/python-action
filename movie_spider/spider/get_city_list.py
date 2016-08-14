# coding=utf-8
from requests import get, post

from spider import selflib


def get_from_url():
    params = {'activityId': '', '_ksTS': selflib.get_timestamp_13(), 'action': 'cityAction', 'n_s': 'new',
              'event_submit_doGetAllRegion': 'true'}
    req = get('https://dianying.taobao.com/cityAction.json', params=params)
    return req.json()
