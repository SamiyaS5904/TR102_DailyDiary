""" 
WEB APP DEV WITH FLASK 

1. USER AUTHENTICATION MODULE 
   -> REGISTER A USER (register.html)
   -> LOGIN A USER (index.html)
   -> Take the user to the HOME Page upon login, register

USE BOOTSTRAP/ TAILWIND CSS AS PER YOUR CONVINIENCE (CSS FRAMEWORK)   
   
"""

# DECORATOR DESIGN PATTERN --- (HOW WIL THIS TEMPLATE LOOK IN UI, IT IS BY -----)
from flask import Flask, render_template

from Day_26_1 import MongoDBHelper
from Day_27_2 import User

web_app = Flask("Doctor's App")
db = MongoDBHelper()
MongoDBHelper.select_db(db_name='Agentic_AI', collection='training')

# Root route
@web_app.route('/')
def index():
    return render_template('index.html')

# Register route
@web_app.route('/register')
def register():
    return render_template('register.html')

@web_app.route('/add-user')
def add_user_in_db():

def main():
    # Secret Key is used for session management
    web_app.secret_key = 'doctors-app-key-v1'
    web_app.run()

if __name__ == '__main__':
    main()
