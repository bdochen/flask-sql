from flask import Flask, render_template_string,  session, request, redirect, url_for,render_template,flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/data.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config["SQLALCHEMY_ECHO"] = False

db = SQLAlchemy(app)



def data_to_sqlite(obj):
    try:
        db.session.add(obj)
        db.session.commit()
        print("数据库写入成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        flash("数据库写入失败")

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), unique=True)

    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):

        self.username = username

        self.email = email

    def __repr__(self):

        return '<User %r>' % self.username
# db.create_all()

user=User(username="hfsdfd3esfahahh", email="hiji23i@qq.com")
data_to_sqlite(user)

users = User.query.all()
for u in users:
    print(u.username,u.email)
