# WEB APP DEVELOPMENT WITH FLASK 

"""
    STEPS:
    1. Install Flask Library  pip install flask 
    2. 
    3.
    4. 
"""

from flask import *                          # it means we are importing everything from flask
web_app = Flask("Doctor's App")

# @web_app.route --> decorators in python 

@web_app.route('/')          # / may be used or may not be it will open same link only

def index():
    return 'Welcome to My First Flask Web App'

def main():
    pass

if __name__ == 'main':
    web_app.