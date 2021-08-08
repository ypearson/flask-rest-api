from flask import Flask, request, abort
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer(), nullable=False)
    likes = db.Column(db.Integer(), nullable=False)

    def __repr__(self) -> str:
        return f'Video(name={self.name}, views={self.views}, likes={self.likes})'
        # return f'**REPR****'

# db.create_all()

video_post_args = reqparse.RequestParser()
video_post_args.add_argument(
    "name",
    type=str,
    help="Name of the video is required",
    required=True)
video_post_args.add_argument(
    "views",
    type=int,
    help="Views of the video is required",
    required=True)
video_post_args.add_argument(
    "likes",
    type=int,
    help="Likes of the video is required",
    required=True)

video_post_args_patch = reqparse.RequestParser()
video_post_args_patch.add_argument(
    "name",
     type=str,
     help="Name of the video is required",
     required=False)
video_post_args_patch.add_argument(
    "views",
     type=int,
     help="Views of the video is required",
     required=False)
video_post_args_patch.add_argument(
    "likes",
     type=int,
     help="Likes of the video is required",
     required=False)

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer,
}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, "Not Found")
        return result, 200

    @marshal_with(resource_fields)
    def post(self, video_id):
        print(request.form)
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, "Conflict resource already exists")
        args = video_post_args.parse_args()
        video = VideoModel(
            id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def patch(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, "Not Found")
        args = video_post_args_patch.parse_args()
        print(args)
        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']
        print("result")
        print(result)
        print("result")
        db.session.commit()
        return result, 201

    def delete(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            VideoModel.query.filter_by(id=video_id).delete()
            db.session.commit()
        else:
            abort(404, "Not Found")
        return '', 200


api.add_resource(Video, "/api/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)


# https://www.restapitutorial.com/lessons/httpmethods.html
# https://www.youtube.com/watch?v=GMppyAPbLYk
