from time import localtime, strftime
from flask import Flask, request
from db import db
import dao
import json

app = Flask(__name__)
db_filename = "twitch.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code

def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code


db.init_app(app)
with app.app_context():
    db.create_all()


# your routes here
@app.route("/")
@app.route("/channels/")
def get_channels():
    return success_response(dao.get_all_channels())

@app.route('/channels/', methods=['POST'])
def post_create_channel():
    body = json.loads(request.data)
    channel = dao.create_channel(
        name = body.get('name')
    )
    return success_response(channel,201)

@app.route("/channels/<int:id>/")
def get_specific_channel(id):
    channel = dao.get_channel_by_id(id)
    if channel is None:
        return failure_response("Channel not found!")
    return success_response(channel)

@app.route('/channels/<int:id>/', methods=['DELETE'])
def del_specific_channel(id):
    channel = dao.del_channel_by_id(id)
    if channel is None:
        return failure_response("Channel not found!")
    return success_response(channel)

@app.route('/users/', methods=['POST'])
def post_create_user():
    body = json.loads(request.data)
    user = dao.create_user(
        name = body.get('name'),
        channel_tag = body.get('tag')
    )
    return success_response(user, 201)

@app.route('/users/<int:id>/')
def get_specific_user(id):
    user = dao.get_user_by_id(id)
    if user is None:
        return failure_response("User not found!")
    return success_response(user)

@app.route('/channel/<int:id>/add/', methods=['POST'])
def post_user_to_channel(id):
    body = json.loads(request.data)
    channel = dao.add_user_to_channel(id, body.get('user_id'), body.get('type'))
    if channel is None:
        return failure_response('Channel or User not found!')
    return success_response(channel)
     

@app.route('/channel/<int:id>/video/', methods=['POST'])
def post_create_video(id):
    body = json.loads(request.data)
    video = dao.create_video(
        channel_id = id,
        title = body.get('title'),
        upload_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
    )
    if video is None:
        return failure_response('Channel not found!')
    return success_response(video, 201)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
