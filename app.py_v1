# -*- coding: utf-8 -*-
from flask import Flask
from flask import url_for
app=Flask(__name__)

@app.route('/')
def hello():
  return 'ssssss'
@app.route('/index')
@app.route('/home')
@app.route('/testtea/')
def test():
  return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

# 记得代码头部加# -*- coding: utf-8 -*-
# 网址代码后面尽量带一个/，以便自动补齐如/bank/
@app.route('/bank/')
def we():
  return 'welcome to our bank '
  
@app.route('/user/<name>/')
def user_page(name):
  return 'http://127.0.0.1/user/%s' %name

@app.route('/testme/')
def test_url_for():
  # 下面是一些调用示例（请在命令行窗口查看输出的 URL）：
  print(url_for('user_page', name='greyli'))  # 输出：/user/greyli
  print(url_for('user_page', name='peter'))  # 输出：/user/peter
  print(url_for('we', _external=True))  # 输出完整url
  print(url_for('we'))  # 输出：/test
  return 'hello test'


if __name__=='__main__':
  app.run(debug=True,host='0.0.0.0',port=80)
