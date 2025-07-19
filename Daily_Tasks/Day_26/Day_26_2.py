# USER Class with Validations

# Here we are using 1 Way Encryption (i.e ek baar password bn gya vo abh duabara ni dikh skta user ko , usko reset hi krna hoga)
# Similarly we can use 2 Way Encryption (i.e first it is encrypted then decrypted using a key (eg. whatsapp))

import hashlib             # FOR ENCYPTION FOR PASSWORDS ---
import datetime
class User:

    def __init__(self, name=None, phone=None, email=None, password=None,gender=None, address=None, age=None, created_on=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        self.gender = gender 
        self.address = address
        self.age = age
        self.created_on = datetime.datetime.now()
        print('[User] Object Created...')

    def input_user_details(self):
    # Logic: let user run inside a loop till the time he dosent enters correct details   

        # CHECKING NAME
        self.name = input('Enter Your Name: ')
        if len(self.name) == 0:
            errors.append('[Error] Name cannot be empty')

        # CHECKING PHONE NUMBER
        self.phone = input('Enter Your Phone: ')
        if len(self.phone) != 10:
            errors.append('[Error] Phone Number must be 10 Digits')

        # CHECKING EMAIL
        if len(self.email) == 0:
            errors.append('[Error] Email Cannot be empty')

        self.email = input('Enter Your Email: ')
        if '@' not in self.email and '.' not in self.email:
            errors.append('[Error] Email is not correct')

        # CHECKING PASSWORD
        self.password = input('Enter Password (Minimum 6 digits): ').encode('utf-8')
        self.password = hashlib.sha256
        if len(self.password) < 6:
            errors.append('[Error] Password must be minimum 6 digits')           # you can add other things also using and,or,---



        # CHECKING ADDRESS
        self.address = input('Enter Your Address: ')
        if len(self.address) ==0:
            errors.append('[Error] Address cannot be empty ')

        # CHECKING AGE    
        self.age = int(input('Enter Your Age: '))
        if self.age < 16:
            errors.append('[Error] Age cannot be less than 15 years')

    # def __str__(self): you have to return string
    def show(self):
        print('~~~~~~~~~~{} Details~~~~~~~~~~'.format(self.name))
        data = 'Phone: {phone} | Email: {email} | Password : {password}\nAddress: {address} Age: {age}'.format_map(vars(self))
        print(data)

    def to_document(self):
        # Return Dictionary representation of the User Object :)
        return vars(self)
    
