# Think of object 
# Visitor : name, class, phone, purpose, meet_to

class Visitor:

    def __init__(self, name=None, phone=None, purpose=None, meet_to=None):
        self.name = name
        self.phone = phone
        self.purpose = purpose
        self.meet_to = meet_to

    def add_visitor(self):
        self.name = input('Enter your name: ')   
        self.phone = input('Enter your Phone Number: ') 
        self.purpose = input('Enter purpose of meet : ')
        self.meet_to = input('Enter person to meet : ')


    def to_csv(self):
        csv = '{},{},{},{}\n'.format(self.name, self.phone, self.purpose, self.meet_to)    
        return csv