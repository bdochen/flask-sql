# -*- coding: UTF-8 -*-
#导入数据库模块
import pymysql
#导入Flask框架，这个框架可以快捷地实现了一个WSGI应用 
from flask import Flask
#默认情况下，flask在程序文件夹中的templates子文件夹中寻找模块
from flask import render_template
#导入前台请求的request模块
from flask import request   
import traceback  
#传递根目录
app = Flask(__name__)

#默认路径访问登录页面
@app.route('/')
def login():
    return render_template('login.html')

#默认路径访问注册页面
@app.route('/regist')
def regist():
    return render_template('regist.html')

#设置响应头
def Response_headers(content):    
    resp = Response(content)    
    resp.headers['Access-Control-Allow-Origin'] = '*'    
    return resp 

#获取注册请求及处理
@app.route('/registuser')
def getRigistRequest():
#把用户名和密码注册到数据库中

    #连接数据库,此前在数据库中创建数据库TESTDB
    db=pymysql.connect(host='127.0.0.1',user='root',password='mysql',port=3306,db='flask')
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    # SQL 插入语句
    sql = 'INSERT INTO crland(user, password) VALUES (%s,%s)'
    user=str(request.args.get('user'))
    print(user)
    password=str(request.args.get('password'))
    print(password)
    try:
        # 执行sql语句
        cursor.execute(sql,(user,password))
        # 提交到数据库执行
        db.commit()
         #注册成功之后跳转到登录页面
        return render_template('login.html') 
    except:
        #抛出错误信息
        traceback.print_exc()
        # 如果发生错误则回滚
        db.rollback()
        return '注册失败'
    # 关闭数据库连接
    db.close()

#获取登录参数及处理
@app.route('/login')
def getLoginRequest():
#查询用户名及密码是否匹配及存在
    #连接数据库,此前在数据库中创建数据库TESTDB
    db=pymysql.connect(host='127.0.0.1',user='root',password='mysql',port=3306,db='flask')
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    # SQL 查询语句
    sql = "select * from crland where user=%s  and password=%s "
    user=str(request.args.get('user'))
    print('user is:',user)
    password=str(request.args.get('password'))
    print('password is:',password)
    try:
        # 执行sql语句
        cursor.execute(sql,(user,password))
        results = cursor.fetchall()
        print('账号及密码匹配个数:',len(results))
        if len(results)==1:
            return '登录成功'
        else:
            return '用户名或密码不正确'
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        traceback.print_exc()
        db.rollback()
    # 关闭数据库连接
    db.close()
    

#使用__name__ == '__main__'是 Python 的惯用法，确保直接执行此脚本时才
#启动服务器，若其他程序调用该脚本可能父级程序会启动不同的服务器
if __name__ == '__main__':
   #app.run(debug=True)
    app.run(debug=True,host='0.0.0.0',port=80)
