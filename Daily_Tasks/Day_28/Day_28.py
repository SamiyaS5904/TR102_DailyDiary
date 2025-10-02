"""
    -> SESSION MANAGEMENT
    Session is used to save the data whenever you need it across the entire application
    The Session Object will be accessible anywhere in the Flask Python Code
"""

# Made using functional programming (not OOP's)

from flask import *
from Day_27_2 import User
from Day_28_1 import Patient
from Day_28_2 import MongoDBHelper
import hashlib

web_app = Flask('Doctors App')
db = MongoDBHelper()

# View
@web_app.route('/')
def index():
    return render_template('index.html')

@web_app.route('/register')
def register():
    return render_template('register.html')

@web_app.route('/home')
def home():
    return render_template('home.html', name=session['name'], email=session['email'])

@web_app.route('/add-patient')
def add_patient():
    return render_template('add-patient.html', name=session['name'], email=session['email'])

# Controller: Add New User
@web_app.route('/add-user', methods=['POST'])
def add_user_in_db():
    user = User()
    user.name = request.form['name']
    user.email = request.form['email']
    user.password = hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()
    user.show()

    db.select_db(db_name="Doctor's_App", collection="Consultations")
    result = db.insert(document=user.to_document())

    if len(str(result.inserted_id)) > 0:
        session['user_id'] = str(result.inserted_id)
        session['name'] = user.name
        session['email'] = user.email
        return render_template('home.html', name=user.name, email=user.email)
    else:
        return 'Something Went Wrong. Please Try Again'

# Controller: Add New Patient
@web_app.route('/add-patient-in-db', methods=['POST'])
def add_patient_in_db():
    patient = Patient()
    patient.name = request.form['name']
    patient.phone = request.form['phone']
    patient.email = request.form['email']
    patient.address = request.form['address']
    patient.gender = request.form['gender']
    patient.age = request.form['age']
    patient.doctor_id = session['user_id']

    db.select_db(db_name="Doctor's_App", collection='Patient')
    result = db.insert(document=patient.to_document())

    if len(str(result.inserted_id)) > 0:
        return render_template('home.html', name=session['name'], email=session['email'])
    else:
        return 'Something Went Wrong. Please Try Again'

# Controller: User Login
@web_app.route('/fetch-user', methods=['POST'])
def fetch_user_from_db():
    query = {
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()
    }

    db.select_db(db_name="Doctor's_App", collection="Consultations")
    documents = db.fetch(query)

    if len(documents) > 0:
        user = documents[0]
        session['user_id'] = str(user['_id'])
        session['name'] = user['name']
        session['email'] = user['email']
        return render_template('home.html', name=user['name'], email=user['email'])
    else:
        return 'Username or Password Invalid. Please Try Again'

# Controller: Fetch All Patients of Logged-in Doctor
@web_app.route('/fetch-patients')
def fetch_patients_from_db():
    query = {
        'doctor_id': session['user_id']
    }

    db.select_db(db_name="Doctor's_App", collection='Patient')
    documents = db.fetch(query)

    if len(documents) > 0:
        return render_template('patients.html', name=session['name'], 
                               email=session['email'], total=len(documents), 
                               patients=documents)
    else:
        return 'Patients Not Found'

# ✅ (Optional) Add Consultation Route
@web_app.route('/add-consultation', methods=['POST'])
def add_consultation():
    consultation = {
        'doctor_id': session['user_id'],
        'patient_id': request.form['patient_id'],
        'diagnosis': request.form['diagnosis'],
        'prescription': request.form['prescription'],
        'notes': request.form['notes']
    }

    db.select_db(db_name="Doctor's_App", collection='Consultations')
    result = db.insert(document=consultation)

    if len(str(result.inserted_id)) > 0:
        return 'Consultation Saved Successfully'
    else:
        return 'Something Went Wrong in Saving Consultation'

# Secret Key for Session
def main():
    web_app.secret_key = 'doctors-app-key-v1'
    web_app.run(port=5001)

if __name__ == '__main__':
    main()
