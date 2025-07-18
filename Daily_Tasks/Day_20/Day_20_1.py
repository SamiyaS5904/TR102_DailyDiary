## MODEL -------- (MVC)

"""    - Think of an object
            - Visitor : serial_no, date_time_stamp, name, address, whome_to_meet, purpose, phone
            - Patient :
            - Customer :
        
"""
import datetime
# VISITOR LOGBOOK

class Visitor:

    def __init__(self,serial_no = None, name = None, address=  None, whome_to_meet= None, purpose = None, phone = None):

        self.serial_no = serial_no
        self.name = name
        self.address = address
        self.whome_to_meet = whome_to_meet
        self.purpose = purpose
        self.phone = phone

    # Automatically pickup date time stamp 
        self.date_time_stamp = str(datetime.datetime.now)

    def input_visitor_details():
        self.name = input('Enter Your Name : ')
        self.phone = input('Enter Your Phone Number : ')
        self.address = input('Enter Your Address : ')
        self.whome_to_meet = input('Enter Person to meet : ')
        self.purpose = input('Enter Purpose of Meeting : ')

    def __str__(self):
        return '{},{},{},{},{},{},{},{}\n'.format(self.serial_no, 
                                                  self.date_time_stamp, 
                                                  self.name, 
                                                  self.phone, 
                                                  self.address, 
                                                  self.whome_to_meet, 
                                                  self.purpose )

