"""
Think of an object: 

Customer : serial_no, name, date_time_stamp,points, phone, address, whom_to_meet, purpose

"""

class Customer:

    def __init__(self ,serial_no=None, name=None, points=None, phone=None, address=None, purpose=None)
        self.serial_no = serial_no
        self.name = name
        self.phone = phone
        self.address = address
        self.purpose = purpose
        self.points = points

def input_customer_details(self):
  #  self.serial_no = serial_no
    self.name = input('Enter your Name : ')
    self.phone = input('Enter Your Name : ')
    self.address = input('Enter Address : ')
    self.whom_to_meet = input('Enter Whom to meet : ')
    self.purpose = input('Enter your purpose of visit : ')
    self.points = input('Enter your loyalty Card Id : ')


