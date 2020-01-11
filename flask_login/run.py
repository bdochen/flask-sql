from flask import Flask, render_template_string,  session, request, redirect, url_for,render_template,flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.secret_key = 'F12Zr47j\3yX R~X@H!jLwf/T'

# 设置过期时间，30秒后失效
app.permanent_session_lifetime =3000000



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def api():
    return 'api is sucessful'

@app.route('/begin')
def begin():
    return render_template('begin.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username =request.form.get('username')
        password = request.form.get('password')
        print(username,' ',password)
        if username=='a' and password=='a':
            session.permanent = True
            session['username']=username
            return redirect(url_for('home'))
        else:
            flash('用户名或密码不正确,请检查!')
            return render_template('login.html')

@app.route('/home/', methods=['GET', 'POST'])
def home():
    if 'username' in session and session['username']=='a':
        #return session['username']
        return render_template('index.html',username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/logout/', methods=['GET'])
def logout():
    # session.pop('username', None)
    session.clear()
    return redirect(url_for('login'))




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)


