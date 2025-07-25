# DOCTORS APP USING FLASK 
        # with updated features
        #    -> logout

# Made using functional programming (not OOP's)

from requests import session
from flask import *
from Day_27_2 import User
from Day_28_1 import Patient
from Day_28_2 import MongoDBHelper
import hashlib
from bson.objectid import ObjectId     # its an inbuilt module of MongoDB

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
    if len(session['user_id']) > 0:
        return render_template('home.html', name=session['name'], email=session['email'])
    else:
        return redirect('/')


@web_app.route('/add-patient')
def add_patient():
    if len(session['user_id']) > 0:
        return render_template('add-patient.html', name=session['name'], email=session['email'])
    else:
        return redirect('/')

#CONTROLLER : LOGOUT
@web_app.route('/logout')
def logout():
    #make values empty for the keys in the Web App
    session['user_id'] = ''
    session['name'] = ''
    session['email'] = ''
    return redirect ('/')

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
        return render_template('error.html', message='Something Went Wrong. Please Try Again', name=session['name'], email=session['email'])

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

    print(patient.to_document())

    db.select_db(db_name="Doctor's_App", collection='Patient')
    result = db.insert(document=patient.to_document())

    if len(str(result.inserted_id)) > 0:
        return render_template('home.html', name=session['name'], email=session['email'])
    else:
        return render_template('error.html', message='Something Went Wrong. Try Again', name=session['name'], email=session['email'])


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
        # In this scenario, whenever user will enter invalid credentials
        # He will see error page, but with navigation menu
        # explore if condition in Flask HTML Template.
        # HW: based on if condition, hide the navigation menu in HTML file
            return render_template('error.html', message='Username or Password Invalid. Please Try Again', name=session['name'], email=session['email'])

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
            return render_template('error.html', message='Patients Not Found', name=session['name'], email=session['email'])
     
# We'll be deleting patients on basis of object id
# recives an inputt in the url

@web_app.route('/delete-patient/<id>')
def delete_patient(id):
    db.select_db(collection='patients')
    query = {'_id': ObjectId(id)}
    result = db.delete(query)
    if result.deleted_count > 0:
        return render_template('success.html', message='Patient Deleted Successfully', name=session['name'], email=session['email'])
    else:
        return render_template('error.html', message='Patient Deletion Failed. Try Again', name=session['name'], email=session['email'])

@web_app.route('/update-patient/<id>')
def update_patient(id): 

    # Temporary Save Patient ID in Session
    # Because in order to update patient, in orther db fucntion
    # we would need patient id
    session['patient_id'] = id

    db.select_db(collection='patients')    
    query = {'_id': ObjectId(id)}
    documents = db.fetch(query)
    if len(documents) > 0:
        patient_document = documents[0]
        return render_template('update-patient.html', 
                               name=session['name'], 
                               email=session['email'],
                               patient=patient_document)
    else:
        return render_template('error.html', message='Patient Not Found. Somethiwng Went Wrong. Try Again', name=session['name'], email=session['email'])


# Controller
@web_app.route('/update-patient-in-db', methods=['POST'])
def update_patient_in_db():

    if len(session['user_id']) > 0:

        patient = Patient()
        patient.name = request.form['name']
        patient.phone = request.form['phone']
        patient.email = request.form['email']
        patient.address = request.form['address']
        patient.gender = request.form['gender']
        patient.age = request.form['age']
        patient.doctor_id = session['user_id'] # Doctor ID
    
        print(patient.to_document())

        db.select_db(collection='patients')
        query = {'_id': ObjectId(session['patient_id'])}

        result = db.update(query, patient.to_document())

        if len(str(result.modified_count)) > 0:
            return render_template('success.html', message='Patient {} Updated successfully in the system'.format(patient.name), name=session['name'], email=session['email'])
        else:
            return render_template('error.html', message='Something Went Wrong. Try Again', name=session['name'], email=session['email'])
    
    else:
        return redirect('/')

def main():
    web_app.secret_key = 'doctors-app-key-v1'
    web_app.run(port=5001)

if __name__ == '__main__':
    main()