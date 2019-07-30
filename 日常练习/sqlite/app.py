# -*- coding: utf-8 -*-
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)





app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    
class Movie(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(60))
    year=db.Column(db.String(4))
'''
user1 = User(name='Grey Li')
user2=User(name='华润')
m1 = Movie(title='让子弹飞', year='1994')
m2 = Movie(title='罗马假日', year='1996') 
m3 = Movie(title='英雄',year='2019')

    db.drop_all()
    db.session.commit()
    db.create_all()
    db.session.add(m1)
    db.session.add(user1)
    db.session.add(m3)
    db.session.add(user2)
    db.session.commit()
'''
@app.route('/')
def index():
    return  '<br> <br> <h1 align="center" style="font-size:180px" >欢迎访问</h1>'


@app.route('/index/')
def ls():
    user = User.query.first()  # 读取用户记录
    movies = Movie.query.all()  # 读取所有电影记录
    print(user.name)
    return render_template('index.html', user=user, movies=movies)

user = User.query.first()
print(user.name)

app.run(debug=True,host='0.0.0.0',port=80)



'''
if __name__=='__main__':

    movie = Movie.query.first()
    print(movie.title,movie.year)
    app.run(debug=True,host='0.0.0.0',port=80)
'''
    
    
