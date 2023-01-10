from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/tinko', methods=['GET'])
def tinko():
    return render_template('tinko.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
