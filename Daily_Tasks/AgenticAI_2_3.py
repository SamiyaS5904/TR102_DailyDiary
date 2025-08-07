# CRUD OPERATIONS OF MONGODB USING OPENAI 

from Day_28_2 import MongoDBHelper
import datetime

db = MongoDBHelper()
db.select_db(db_name='AgenticAI')



def get_patient_by_phone(phone_number):
    db.select_db(collection='aipatient')

    documents = db.fetch(query ={'phone': phone})
    if len(documents)>0:
        return documents[0]
    else:
        return 'No Patient Found with Phone {}'.format(phone)


def add_patient(name,phone,email,gender,age,symptoms):
    db.select_db(collection='aipatient')
    
    patient = {
        'name' : name,
        'phone' : phone,
        'email' : email,
        'gender' : gender,
        'age' : age,
        'symptoms' : symptoms,
        'created_on' : datetime.datetime.now()
    }

    result = db.insert(patient)
    if result.inserted_id:
        return '{} added to the system with phone : {}'.format(name, phone)
    

def save_consultation(phone, medicines, remarks):
    db.select_db(collection='aiconsultation')

    consultation = {
        'phone' : phone, 
        'medicines' : medicines,
        'remarks' : remarks,
    }

    result = db.insert(consultation)
    if result.inserted_id:
        return '{} added to the system with phone: {}'.format(name, phone)