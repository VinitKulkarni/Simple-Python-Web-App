from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    requests.post('http://backend:5000/add_user', json={'username': username})
    return 'User added!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
