from flask import Flask, render_template, request, redirect, url_for
from codes.login import check_login
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def initialize():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        login_res = check_login(request.form['email'], request.form['password'])
        if login_res == 200:
            return redirect(url_for('index'))
        else:
            return render_template('login.html')

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/test', methods=['GET'])
def test():
    return render_template('test.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
