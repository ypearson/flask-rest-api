from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {
'tim':{'age':19, 'gender':'male'},
'john':{'age':29, 'gender':'male'}}

class HelloWorld(Resource):
    def get(self, name):
        return names[name]

    def post(self):
        return {"response":"this is a post"}

# api.add_resource(HelloWorld, "/api")
api.add_resource(HelloWorld, "/api/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)



# https://www.youtube.com/watch?v=GMppyAPbLYk