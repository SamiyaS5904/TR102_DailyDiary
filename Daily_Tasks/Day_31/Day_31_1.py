# - Consultation :
#       bp low, bp high, sugar, temperature, height, weight, allergies, follow_up


class Consultation:

    def __init__(self, bp_low=80, bp_high=120, sugar=80, temperature=98.4, 
                 height='', weight='', allergies='', medicines='',
                 chief_complaints='', follow_up='', doctor_id='', patient_id=''):
    
        self.bp_low = bp_low
        self.bp_high = bp_high
        self.sugar = sugar
        self.temperature = temperature
        self.height = height
        self.weight = weight
        self.allergies = allergies
        self.medicines = medicines
        self.chief_complaints = chief_complaints
        self.follow_up = follow_up
        self.doctor_id = doctor_id
        self.patient_id = patient_id

    def to_document(self):
        return {
            'weight': self.weight,
            'height': self.height,
            'bp_low': self.bp_low,
            'bp_high': self.bp_high,
            'sugar': self.sugar,
            'temperature': self.temperature,
            'chief_complaints': self.chief_complaints,
            'allergies': self.allergies,
            'medicines': self.medicines,
            'follow_up': self.follow_up
        }


    def to_document(self):
        return vars(self)    
    

    