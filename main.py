from flask import Flask
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser

app = Flask(__name__)
api = Api(app, prefix="/api/v1")

users = [
    {"email": "sant@gmail.com", "name": "Saint Kay", "id": 1}
]

def get_user_by_id(user_id):
    for x in users:
        if x.get("id") == int(user_id):
            return x

subscriber_request_parser = RequestParser(bundle_errors=True)
subscriber_request_parser.add_argument("name", type=str, required=True, help="Name has to be valid string")
subscriber_request_parser.add_argument("email", required=True)
subscriber_request_parser.add_argument("id", type=int, required=True, help="Please enter valid integer as ID")

class SubscriberCollection(Resource):
    def get(self):
        return users

    def post(self):
        args = subscriber_request_parser.parse_args()
        users.append(args)
        return {"msg": "Subscriber added", "subscriber": args}

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
