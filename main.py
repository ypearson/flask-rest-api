from flask import Flask, request, abort
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

# 200 --> OK
# 201 --> Created
# 404 --> Not Found
# 409 --> Conflict if resource already exists

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database'
db = SQLAlchemy(app)


video_post_args = reqparse.RequestParser()
video_post_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_post_args.add_argument("views", type=int, help="Views of the video is required", required=True)
video_post_args.add_argument("likes", type=int, help="Likes of the video is required", required=True)

videos={}

def abort_if_video_doesnot_exist(video_id):
    if video_id not in videos:
        print("Not Found")
        abort(404, "Not Found")

def abort_if_video_exist(video_id):
    if video_id in videos:
        print("Conflict resource already exists")
        abort(409, "Conflict resource already exists")

class Video(Resource):
    def get(self, video_id):
        abort_if_video_doesnot_exist(video_id)
        return videos[video_id], 200

    def post(self, video_id):
        print(request.form)
        args = video_post_args.parse_args()
        abort_if_video_exist(video_id)
        videos[video_id] = args
        print("POST")
        print(videos)
        return videos[video_id], 201

    def delete(self, video_id):
        abort_if_video_doesnot_exist(video_id)
        video = videos.pop(video_id, 'No Key found')
        print("DELETE")
        print(videos)
        return '', 200

api.add_resource(Video, "/api/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)


# https://www.restapitutorial.com/lessons/httpmethods.html
# https://www.youtube.com/watch?v=GMppyAPbLYk
