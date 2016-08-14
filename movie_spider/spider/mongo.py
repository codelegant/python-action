from pymongo import MongoClient


class Taobao:
    """数据库的相关操作"""

    def __init__(self):
        db_config = {'host': 'localhost', 'port': 1992, 'username': 'elegant', 'password': '920527'}
        client = MongoClient(db_config['host'], db_config['port'])
        self.db = client['taobao']
        try:
            self.db.authenticate(db_config['username'], db_config['password'], mechanism='SCRAM-SHA-1')
        finally:
            print('用户登录数据库 tabao 失败')

    def get(self, collection, params={}):
        return self.db[collection].find(params)

    def insert(self, collection, params={}):
        return self.db[collection].insert(params)