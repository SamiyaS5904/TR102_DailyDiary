
from flask import *
from Day_27_2 import User
from Day_28_1 import Patient
from Day_28_2 import MongoDBHelper
from Day_31_1 import Consultation
import hashlib
from bson.objectid import ObjectId

web_app = Flask('Doctors App')
db = MongoDBHelper()
db.select_db(db_name="Doctor's_App", collection='users')

@web_app.route('/')
def index():
    return render_template('index.html')

@web_app.route('/register')
def register():
    return render_template('register.html')

@web_app.route('/search-patient', methods=['POST'])
def search_patient_in_db():
    search = request.form['search']

    db = client["Doctor's_App"]
patients_collection = db.select_collection("Patient")

# 2. Get search input
search_type = input("Search by 'name' or 'phone': ").strip().lower()
search_value = input("Enter the value to search: ").strip()

# 3. Build query
query = {}

if search_type == "phone":
    query = {"phone": search_value}

elif search_type == "name":
    # Case-insensitive partial match using regex
    query = {"name": {"$regex": search_value, "$options": "i"}}

else:
    print("Invalid search type. Choose 'name' or 'phone'.")
    exit()

# 4. Execute query
results = patients_collection.find(query)

# 5. Display results
found = False
for patient in results:
    found = True
    print("---- Patient Found ----")
    print(f"Name: {patient.get('name')}")
    print(f"Phone: {patient.get('phone')}")
    print(f"Other Info: {patient}")  # can customize what to show

if not found:
    print("No matching patient found.")















@web_app.route('/home')
def home():
    if len(session.get('user_id', '')) > 0:
        return render_template('home.html', name=session['name'], email=session['email'])
    else:
        return redirect('/')

@web_app.route('/add-patient')
def add_patient():
    if len(session.get('user_id', '')) > 0:
        return render_template('add-patient.html', name=session['name'], email=session['email'])
    else:
        return redirect('/')

@web_app.route('/add-consultation/<id>')
def add_consultation(id):
    session['patient_id'] = id

    db.select_db(collection='patients')
    query = {'_id': ObjectId(id)}
    patient = db.fetch(query)[0] if db.fetch(query) else None

    if patient and len(session.get('user_id', '')) > 0:
        return render_template('add-consultation.html', name=session['name'], email=session['email'], patient_name=patient['name'])
    else:
        return redirect('/')


@web_app.route('/logout')
def logout():
    session['user_id'] = ''
    session['name'] = ''
    session['email'] = ''
    return redirect('/')


@web_app.route('/add-user', methods=['POST'])
def add_user_in_db():
    user = User()
    user.name = request.form['name']
    user.email = request.form['email']
    user.password = hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()

    db.select_db(collection='users')
    result = db.insert(user.to_document())

    if result.inserted_id:
        session['user_id'] = str(result.inserted_id)
        session['name'] = user.name
        session['email'] = user.email
        return render_template('home.html', name=user.name, email=user.email)
    else:
        return render_template('error.html', message='Something Went Wrong. Please Try Again', name='', email='')


@web_app.route('/add-patient-in-db', methods=['POST'])
def add_patient_in_db():
    if len(session.get('user_id', '')) > 0:
        patient = Patient()
        patient.name = request.form['name']
        patient.phone = request.form['phone']
        patient.email = request.form['email']
        patient.address = request.form['address']
        patient.gender = request.form['gender']
        patient.age = request.form['age']
        patient.doctor_id = session['user_id']

        db.select_db(collection='patients')
        result = db.insert(patient.to_document())

        if result.inserted_id:
            return render_template('success.html', message=f'Patient {patient.name} added successfully in the system', name=session['name'], email=session['email'])
        else:
            return render_template('error.html', message='Something Went Wrong. Try Again', name=session['name'], email=session['email'])

    return redirect('/')


@web_app.route('/add-consultation-in-db', methods=['POST'])
def add_consultation_in_db():
    if len(session.get('user_id', '')) > 0:
        consultation = Consultation()
        consultation.weight = request.form['weight']
        consultation.height = request.form['height']
        consultation.bp_low = request.form['bp_low']
        consultation.bp_high = request.form['bp_high']
        consultation.sugar = request.form['sugar']
        consultation.temperature = request.form['temperature']
        consultation.chief_complaints = request.form['chief_complaints']
        consultation.allergies = request.form['allergies']
        consultation.medicines = request.form['medicines']
        consultation.follow_up = request.form['follow_up']
        consultation.patient_id = session['patient_id']
        consultation.doctor_id = session['user_id']

        db.select_db(collection='consultations')
        result = db.insert(consultation.to_document())

        if result.inserted_id:
            return render_template('success.html', message=f'Consultation for {consultation.medicines} added successfully.', name=session['name'], email=session['email'])
        else:
            return render_template('error.html', message='Something Went Wrong. Try Again', name=session['name'], email=session['email'])

    return redirect('/')


@web_app.route('/fetch-user', methods=['POST'])
def fetch_user_from_db():
    query = {
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()
    }

    db.select_db(collection='users')
    documents = db.fetch(query)

    if documents:
        user = documents[0]
        session['user_id'] = str(user['_id'])
        session['name'] = user['name']
        session['email'] = user['email']
        return render_template('home.html', name=user['name'], email=user['email'])
    else:
        return render_template('error.html', message='Invalid Credentials', name='', email='')


@web_app.route('/fetch-patients')
def fetch_patients_from_db():
    if len(session.get('user_id', '')) > 0:
        query = {'doctor_id': session['user_id']}
        db.select_db(collection='patients')
        patients = db.fetch(query)

        if patients:
            return render_template('patients.html', name=session['name'], email=session['email'], total=len(patients), patients=patients)
        else:
            return render_template('error.html', message='No Patients Found', name=session['name'], email=session['email'])

    return redirect('/')


def main():
    web_app.secret_key = 'doctors-app-key-v1'
    web_app.run(port=5001)

if __name__ == '__main__':
    main()
