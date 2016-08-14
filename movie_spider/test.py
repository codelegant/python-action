# from resource.city import get
from resource.city import get
from resource import User
from flask_restful import Api
from flask import Flask

print(get())
app = Flask(__name__)
api = Api(app, catch_all_404s=True)
api.add_resource(User, '/user/<int:id>', '/user', '/user/')
if __name__ == '__main__':
    app.run(debug=True)