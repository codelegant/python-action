from flask import Flask, got_request_exception
from random import random
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with, wraps
from resource.city import get

print(get())


def log_exception(sender, exception, **kwargs):
    sender.logger.debug('Got exception during processing:%s', exception)
    print('some error occured')


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in todos:
        abort(404, message='Todo {} doesn\'t exist'.format(todo_id))


def odd_number(value):  # 定义一种输入类型
    if int(value) % 2 == 0:  # turn string into int
        raise ValueError('Value is not odd')
    return value


def basic_authentication():
    return 'This is a basic authentication function'


def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not getattr(func, 'authenticated', True):
            return func(*args, **kwargs)
        acct = basic_authentication()
        if acct:
            return func(*args, **kwargs)

    return wrapper


class AllCapsString(fields.Raw):  # 自定义输出过滤
    def format(self, value):
        return value.upper()


class UrgentItem(fields.Raw):
    def format(self, value):
        return 'Urgent' if value & 0b01 else 'Normal'  # 判断第一位，如果是 1 'Urgent'，否则  'Normal'


class UnreadItem(fields.Raw):
    def format(self, value):
        return 'Unread' if value & 0b10 else 'Read'  # 判断第二位，如果是 1  'Unread'，否则   'Read'


class RandomNumber(fields.Raw):
    def output(self, key, obj):
        return random()


# got_request_exception(log_exception, app)

todos = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '??????'},
    'todo3': {'task': 'profit!'}
}

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('task', type=str, help='task参数不正确')
parser.add_argument('odd', type=odd_number)


class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return todos[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del todos[todo_id]
        return '', 204

    def put(self, todo_id):
        # request.form['task']
        args = parser.parse_args(strict=True)
        task = {'task': args['task']}
        todos[todo_id] = task
        return task, 201


class TodoList(Resource):
    def get(self):
        return todos

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(todos.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        todos[todo_id] = {'task': args['task']}
        return todos[todo_id], 201


class Mask(Resource):
    resource = {
        'firstName': 'lai',
        'flag': 0b00,
        # 'lastName': 'chuanfeng',
    }
    resource_fields = {
        'name': fields.String(attribute='firstName'),  # 重命名键值
        'lastName': fields.String(default='chuanfeng'),  # 设置默认值
        'priority': UrgentItem(attribute='flag'),
        'status': UnreadItem(attribute='flag'),
        'uri': fields.Url('mask'),
        'random': RandomNumber,
    }

    def post(self):
        args = parser.parse_args()
        return args

    @marshal_with(resource_fields)  # 将键值转化为指定格式的装饰器,如果加入envelope='resource'，则使用resource封装
    def get(self):
        return Mask.resource, 410


class Address(Resource):
    resource = {
        'name': 'lai',
        'addr1': '123 fake street',
        'addr2': '',
        'city': 'New York',
        'state': 'NY',
        'zip': '10468'
    }
    resource_filed = {
        'name': fields.String(attribute='name'),
        'address': {
            'line1': fields.String(attribute='addr1'),
            'line2': fields.String(attribute='addr2'),
            'city': fields.String,
            'state': fields.String,
            'zip': fields.String,
        }
    }

    @marshal_with(resource_filed)
    def get(self):
        return Address.resource