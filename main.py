from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app, prefix="/api/v1")

users = [
    {"email": "sant@gmail.com", "name": "Saint Kay", "id": 1}
]

class SubscriberCollection(Resource):
    def get(self):
        return {"msg": "All subscribers"}



api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
