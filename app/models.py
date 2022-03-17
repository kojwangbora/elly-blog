from app import db
from flask_login import UserMixin
from datetime import datetime





class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(), nullable = False)
    password =db.Column(db.String(80))
    bio = db.Column(db.String(255), default = 'You bio  is empty')
    image_url = db.Column(db.String(), default =' profile.jgp')
    posts = db.relationship('Posts', backref = 'author', lazy = 'dynamic')
    comments = db.relationship('Comments', backref = 'commentator', lazy = 'dynamic')


class Posts (db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(20), nullable = False)
    content = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime(), index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))




    # @property
    # def password(self):
    #     raise ValidationError('Password cannot be read')


    # @password.setter
    # def password(self,password):
    #         self.password_hash = generate_password_hash(password)


    # def verify_password(self,password):
    #     check_password_hash(self.password_hash, password)
     

    def __repr__(self):
        return '<User %r>' % self.username

class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False)
    comment = db.Column(db.String(255), nullable = False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))