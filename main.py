from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self, myParam, number):
        return {"data":"Hello World " + myParam + str(number)}

    def post(self):
        return {"response":"this is a post"}

# api.add_resource(HelloWorld, "/api")
api.add_resource(HelloWorld, "/api/<string:myParam>/<int:number>")

if __name__ == "__main__":
    app.run(debug=True)

