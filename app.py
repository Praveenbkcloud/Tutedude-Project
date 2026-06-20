from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
import json

app = Flask(__name__)

# MongoDB Atlas Connection String
MONGO_URI = "mongodb+srv://praveenbkcloud_db_user:I3w23NbYOPUNUPGj@flaskproject.sf4cvqp.mongodb.net/?appName=Flaskproject"

client = MongoClient(MONGO_URI)
db = client["studentdb"]
collection = db["students"]

# API Route
@app.route('/api')
def get_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/todo')
def todo():
    return render_template('todo.html')

# Form Submission
@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']

        collection.insert_one({
            "name": name,
            "email": email
        })

        return redirect(url_for('success'))

    except Exception as e:
        return render_template('index.html', error=str(e))

# Success Page
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)