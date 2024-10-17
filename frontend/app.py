from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        requests.post('http://be:5000/add_user', json={'username': username})
    
    # Fetch updated user list
    users = requests.get('http://be:5000/').json()
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
