from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'User_Table'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class Pose(db.Model):
    __tablename__ = 'Pose_Table'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User_Table.id'), nullable=False)
    pose_data = db.Column(db.Text, nullable=False)
    feedback = db.Column(db.Text, nullable=True)

class Feedback(db.Model):
    __tablename__ = 'Feedback_Table'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User_Table.id'))
    pose_id = db.Column(db.Integer, db.ForeignKey('Pose_Table.id'))
    feedback_text = db.Column(db.String(255))
