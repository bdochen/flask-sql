#导入模块
# -*- coding: utf-8 -*-
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql

#创建flask对象
app = Flask(__name__)

@app.route('/')
def index():
    return '<br> <br><h1 align="center" style="font-size:200px" >welcome  </h1>'



#SQLALCHEMY_DATABASE_URI   THE LAST IS URI NOT  URL
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:mysql@127.0.0.1/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_ECHO'] = True
print('mysql connect sucess')
db=SQLAlchemy(app)

#  daxie M   in the word Model
class Roles(db.Model):


###############################################
    # 创建数据表，定义表名,重点，这个是重点
    __tablename__ = 'crland_oa'
###############################################
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    #repr()方法显示一个可读字符串
    def __repr__(self):
        return '<Crland: %s %s>' % (self.name, self.id)




if __name__=='__main__':
    db.create_all()
    app.run(debug=True,host='0.0.0.0',port=80)
