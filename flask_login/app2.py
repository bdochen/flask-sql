from flask import Flask, render_template_string,  session, request, redirect, url_for,render_template,flash
import datetime
import os
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.permanent_session_lifetime =300000
app.config['SECRET_KEY'] = os.urandom(24)
#app.config['SECRET_KEY'] = 'F12Zr47j\3yX R~X@H!jLwf/T'

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
        # print(e)
        db.session.rollback()
        print("数据库写入失败")

# 定义会员模型
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 昵称
    pwd = db.Column(db.String(100))  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    phone = db.Column(db.String(11), unique=True)  # 手机号码
    info = db.Column(db.Text)  # 个性简介
    face = db.Column(db.String(255), unique=True)  # 头像
    add_time = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)  # 添加时间
    uuid = db.Column(db.String(255), unique=True)  # 唯一标识符
    comment = db.relationship('Comment', backref='user')  # 会员日志外键关系关联，backref互相绑定user表

    def __repr__(self):  # 查询的时候返回
        return "<User %r>" % self.name


# 评论
class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    content = db.Column(db.Text)  # 评论内容
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属用户，在user表中创建外键关联
    add_time = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)  # 添加时间
    def __repr__(self):
        return "<Comment %r>" % self.id



# 电影
class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255), unique=True)  # 标题
    url = db.Column(db.String(255), unique=True)  # 播放地址
    info = db.Column(db.Text)  # 简介
    logo = db.Column(db.String(255), unique=True)  # 封面
    star = db.Column(db.SmallInteger)  # 星级
    play_num = db.Column(db.BigInteger)  # 播放量
    comment_num = db.Column(db.BigInteger)  # 评论量
    area = db.Column(db.String(255))  # 上映地区
    release_time = db.Column(db.Date)  # 上映时间
    length = db.Column(db.String(100))  # 播放时长
    add_time = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)  # 添加时间
    def __repr__(self):
        return "<Movie %r>" % self.title

#user=User(name='chen', pwd='xiao', email='chen@qq.com')
#data_to_sqlite(user)






@app.route('/')
def index():
    #return render_template('index.html')
     return redirect(url_for('home'))



@app.route('/register/', methods=['GET', 'POST'])
def register():
    #return render_template('index.html')
    if request.method == 'GET':
        return render_template('register.html')
    if  request.method == 'POST':
        username =request.form.get('username')
        password = request.form.get('password')
        email= request.form.get('email')
        auth_name=User.query.filter_by(name=username).first()
        auth_email=User.query.filter_by(email=email).first()
        if not (auth_name)  :
            user = User(name=username,  pwd=password,  email=email)
            data_to_sqlite(user)
            flash('注册成功')
            return render_template('login.html')
        else:
            flash('注册失败')
            return render_template('register.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if  request.method == 'GET':
        return render_template('login.html')
    if  request.method == 'POST':
        username =request.form.get('username')
        password = request.form.get('password')
#       print(username,' ',password)
        auth_name=User.query.filter_by(name=username).first()
        if auth_name and auth_name.pwd==password :
#           print(password)
            session.permanent = True
            session['username']=username
            return redirect(url_for('home'))
        else:
            flash('用户名或密码不正确,请检查!')
            return render_template('login.html')
            
        
#        if username=='a' and password=='a':
#            session.permanent = True
#            session['username']=username
#            return redirect(url_for('home'))
        
#auth_name=User.query.filter_by(name='chen').first()
#print(auth_name.pwd)


#address=Address.query.filter_by(id=3).first()
#print(address.email)



@app.route('/home/', methods=['GET', 'POST'])
def home():
    if 'username' in session:
        #return session['username']
        return render_template('index.html',username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/logout/', methods=['GET'])
def logout():
    # session.pop('username', None)
    session.clear()
    return redirect(url_for('login'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')



@app.errorhandler(500)
def internal_server_error(e):
    render_template('500.html')





if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)








#db.create_all()


# 会员日志
#class UserLog(db.Model):
#    __tablename__ = "userlog"
#    id = db.Column(db.Integer, primary_key=True)  # 编号
#    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属会员
#    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
#    ip = db.Column(db.String(100))  # 登录IP
#    add_time = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)  # 登录时间

#    def __repr__(self):
#        return "<Userlog %r>" % self.id

#class Userlist(db.Model):
#    id=db.Column(db.Integer,primary_key=True)
#    name=db.Column(db.String(200))
#    address=db.relationship('Address',backref='userlist')

#class Address(db.Model):
#    id=db.Column(db.Integer,primary_key=True)
#    email=db.Column(db.String(200),unique=True)
#    user_id=db.Column(db.Integer ,db.ForeignKey('userlist.id'))

    
#address=Address.query.filter_by(id=3).first()
#print(address.email)
#print(address.userlist.name)

#print('-----------------------','/n','-----------------------------')
#userlist=Userlist.query.filter_by(name='li').first()
# print(userlist.address.email) 不能这样使用
#print(userlist.id)


# a=Address.query.filter(Address.id==1).first()
# print(a.email)

# userlist=userlist(name='xiao')
# data_to_sqlite(userlist)
# address=Address(email='xiao@qq.com',user_id=3)
# data_to_sqlite(address)




#user=User(username="hfsdfd3esfahahh", email="hiji23i@qq.com")
#data_to_sqlite(user)

#users = User.query.all()
#for u in users:
#    print(u.username,'----', u.email)