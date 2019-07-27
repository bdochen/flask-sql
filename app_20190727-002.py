# -*- coding: utf-8 -*-
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
app=Flask(__name__)


@app.route('/')
def index():
    return '<h1 align="center" style="font-size:200px" >welcome  </h1>'



#SQLALCHEMY_DATABASE_URI   THE LAST IS URI NOT  URL
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:mysql@127.0.0.1/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_ECHO'] = True
print('mysql connect sucess')
db=SQLAlchemy(app)
#  daxie M   in the word Model

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

def __repr__(self):
    return '<User %r>' % self.username



if __name__=='__main__':
    db.create_all()
    admin = User(username='admin', email='admin@example.com')
    guest = User(username='guest', email='guest@example.com')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
    User.query.all()
    app.run(debug=True,host='0.0.0.0',port=80)
  
