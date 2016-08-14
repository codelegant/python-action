from flask import Flask
from flask_restful import Api
from api.todos import *
from resource import User

errors = {
    'UserAlreadyExistsError': {
        'message': "A user with that username already exists.",
        'status': 409,
    },
    'ResourceDoesNotExist': {
        'message': "A resource with that ID no longer exists.",
        'status': 410,
        'extra': "Any extra information you want.",
    },
    'Not Found': {
        'message': "资源无法访问",
        'status': 404,
        'extra': "Any extra information you want.",
    }
}

app = Flask(__name__)
api = Api(app, catch_all_404s=True, errors=errors)

api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(Mask, '/mask')
api.add_resource(Address, '/address')
api.add_resource(User, '/user/<int:id>', '/user', '/user/')
if __name__ == '__main__':
    app.run(debug=True)