from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host='database',
        user='root',
        password='password',
        database='simple_db'
    )
    return connection

@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.json['username']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username) VALUES (%s)', (username,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'status': 'success'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
