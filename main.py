from flask import Flask
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser

app = Flask(__name__)
api = Api(app, prefix="/api/v1")

users = [
    {"email": "sant@gmail.com", "name": "Saint Kay", "id": 1}
]

class SubscriberCollection(Resource):
    def get(self):
        return {"msg": "All subscribers"}

    def post(self):
        return {"msg": "We will create new subscribers here"}

class Subscriber(Resource):
    def get(self, id):
        return {"msg": "Details about user id {}".format(id)}

    def put(self, id):
        return {"msg": "Update user id {}".format(id)}

    def delete(self, id):
        return {"msg": "Delete user id {}".format(id)}



api.add_resource(SubscriberCollection, '/subscribers')
api.add_resource(Subscriber, '/subcribers/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
