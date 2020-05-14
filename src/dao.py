from db import db, Channel, Video, User

# your methods here

#--Channel-------------------------
def get_all_channels():
    a = [c.serialize() for c in Channel.query.all()]
    return a

def create_channel(name):
    new_channel = Channel(
        name = name
    )
    db.session.add(new_channel)
    db.session.commit()
    return new_channel.serialize()

def get_channel_by_id(channel_id):
    channel = Channel.query.filter_by(id=channel_id).first()
    if channel is None:
        return None
    return channel.serialize()

def del_channel_by_id(channel_id):
    channel = Channel.query.filter_by(id=channel_id).first()
    if channel is None:
        return None
    db.session.delete(channel)
    db.session.commit()
    return channel.serialize()

#--Video-------------------------

def create_video(channel_id, title, upload_time):
    channel = Channel.query.filter_by(id=channel_id).first()
    if channel is None:
        return None
    new_video = Video(channel_id = channel_id, title = title, upload_time = upload_time)
    db.session.add(new_video)
    db.session.commit()
    a = new_video.serialize()
    c = get_channel_by_id(channel_id)
    del c["videos"]
    del c["subscribers"]
    del c["supporters"]
    a["channels"] = c
    return a


#--User-------------------------

def create_user(name,channel_tag):
    new_user = User(name = name, channel_tag=channel_tag)
    db.session.add(new_user) 
    db.session.commit()
    d = new_user.serialize()
    d["channels"] = []
    return d

def get_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    d = user.serialize()
    d["channels"] = user.subchannels + user.supchannels
    return d

def add_user_to_channel(channel_id,user_id,type):
    channel = Channel.query.filter_by(id=channel_id).first()
    if channel is None:
        return None
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        return None
    if type == 'subscriber':
        channel.subscribers.append(user)
        db.session.commit()
    if type == 'supporter':
        channel.supporters.append(user)
        db.session.commit()
    return get_channel_by_id(channel_id)

