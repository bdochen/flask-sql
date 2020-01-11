# -*- coding: utf-8 -*-
from flask import Flask, render_template_string,  session, request, redirect, url_for,render_template,flash, jsonify
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
a=0
app = Flask(__name__)
#db = SQLAlchemy(app)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return render_template('echarts.html')
    
@app.route('/test')
def test():
    return render_template('superecharts.html')

@app.route('/api', methods=['GET', 'POST'])
def api():
    name=["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
    num=[5, 20, 36, 10, 10, 20]
    data={}
    for name_each in name: 
      data[anme_each]=num 
    return jsonify(data)

#return jsonify({'status': '0', 'username': 'chen', 'errmsg': 'sucess'})


@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'sucess'

@app.route('/echarts', methods=['GET', 'POST'])
def echarts():
    name=["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
    num=[5, 20, 36, 10, 10, 20]
    data={}
    data=dict(zip(name,num))
    return jsonify(data)
    #return jsonify({'status': '0', 'username': '陈良伟', 'errmsg': 'sucess'})


    
@app.route('/superecharts', methods=['GET', 'POST'])
def superecharts():
    name=["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
    num=[11, 20, 36, 10, 10, 20]
    global a
    a=a+1
    print(a)
    data={}
    i=0
    while i< len(num):
        num[i]=num[i]+a
        i=i+1
    data={"name":name ,"num":num}
    return jsonify(data)




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)


