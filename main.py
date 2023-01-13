from flask import Flask, render_template, request, redirect, url_for, session
from codes.login import check_login
import const

# CONFIG
app = Flask(__name__)
app.config['SECRET_KEY'] = const.SECRET_KEY
    
# ROUTING
@app.route('/', methods=['GET'])
def initialize():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if 'user' in session:
        return redirect(url_for('index'))
    else:
        if request.method == 'GET':
            return render_template('login.html')
        else:
            login_res = check_login(request.form['username'], request.form['password'])
            if login_res:
                session['user'] = request.form['username']
                return redirect(url_for('index'))
            else:
                return render_template('login.html')

@app.route('/index', methods=['GET'])
def index():
    if 'user' in session:    
        return render_template('index.html')
    else: 
        return redirect(url_for('login'))

@app.route('/test', methods=['GET'])
def test():
    if 'user' in session:    
        return render_template('test.html')
    else: 
        return redirect(url_for('login'))

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/newindex', methods=['GET'])
def nindex():
    return render_template('new_index.html')
# RUN
if __name__ == "__main__":
    app.run(debug=True, port=5000)
