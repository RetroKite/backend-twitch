from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#many-to-many relations

sup_association_table = db.Table('sub_association', db.Model.metadata,
    db.Column('channel_id', db.Integer, db.ForeignKey('channel.id')),
    db.Column('sub_id ', db.Integer, db.ForeignKey('user.id'))
    )

sub_association_table = db.Table('sup_association', db.Model.metadata,
    db.Column('channel_id', db.Integer, db.ForeignKey('channel.id')),
    db.Column('sup_id', db.Integer, db.ForeignKey('user.id'))
    )



# your classes here

class Channel(db.Model):
    __tablename__ = 'channel'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    videos = db.relationship('Video', cascade='delete')
    subscribers = db.relationship('User', secondary=sub_association_table, back_populates='subchannels')
    supporters = db.relationship('User', secondary=sup_association_table, back_populates='supchannels')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'videos': [a.serialize() for a in self.videos],
            'subscribers': [i.serialize() for i in self.subscribers],
            'supporters': [s.serialize() for s in self.supporters] 
        }

class Video(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    upload_time = db.Column(db.Integer, nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'), nullable=False)

    def __init__(self, **kwargs):
        self.title = kwargs.get('title', '')
        self.upload_time = kwargs.get('upload_time','None') 
        self.channel_id= kwargs.get('channel_id')
    
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'upload_time': self.upload_time
        }

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    channel_tag = db.Column(db.String, nullable=False)
    subchannels = db.relationship('Channel', secondary=sub_association_table, back_populates='subscribers')
    supchannels = db.relationship('Channel', secondary=sup_association_table, back_populates='supporters')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name','')
        self.channel_tag = kwargs.get('channel_tag','')
    
    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'tag': self.channel_tag
        }
