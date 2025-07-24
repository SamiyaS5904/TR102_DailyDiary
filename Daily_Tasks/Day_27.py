"""
WEB APP DEV WITH FLASK 
    1.USER AUTHENTICATION MODULE 
        -> REGISTER A USER (register.html)
        -> LOGIN A USER (index.html)
        -> Take the user to the HOME Page upon login, register
"""

import hashlib
from flask import Flask, render_template, request
from Day_26_1 import MongoDBHelper
from Day_27_2 import User

# Flask app
web_app = Flask("Doctor's App")

# MongoDB setup
db_helper = MongoDBHelper()
db = db_helper.select_db(db_name='Agentic_AI', collection='users')

# ROUTES ----------------------------

@web_app.route('/')
def index():
    return render_template('index.html')

@web_app.route('/register')
def register():
    return render_template('register.html')

@web_app.route('/add-user', methods=['POST'])
def add_user_in_db():
    user = User()
    user.name = request.form['name']
    user.email = request.form['email']
    user.password = hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()

    user.show()
    db.insert_one(user.to_document())

    return render_template('home.html')

@web_app.route('/fetch-user', methods=['POST'])
def fetch_user_from_db():
    query = {
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()
    }

    documents = list(db.find(query))
    if len(documents) > 0:
        user = documents[0]
        print(user)
        return render_template('home.html')
    else:
        return "Invalid email or password", 401

# MAIN --------------------------------
def main():
    web_app.secret_key = 'doctors-app-key-v1'
    web_app.run(port=5002, debug=True)

if __name__ == '__main__':
    main()
