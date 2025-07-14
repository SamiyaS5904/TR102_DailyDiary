# DOCTOR's APP

# 1. Patient 
# 2. Consulation

"""
1 Patient Has a Relation with Consulations


Patient : patient_id, name, phone, email, address, dob, gender, created_on


"""

class Patient:

    def __init__(self,
                 name = None,
                 phone = None,
                 email =  None,
                 address = None,
                 dob = None, 
                 gender = None,
                 ):
        
        self.patient_id=0
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.dob = dob
        self.gender = gender


