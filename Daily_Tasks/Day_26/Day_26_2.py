import hashlib
import datetime

class User:

    def __init__(self, name=None, phone=None, email=None, password=None, gender=None, address=None, age=None, created_on=None):
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
        errors = []  # ✅ define before using

        self.name = input('Enter Your Name: ')
        if len(self.name.strip()) == 0:
            errors.append('[Error] Name cannot be empty')

        self.phone = input('Enter Your Phone: ')
        if len(self.phone.strip()) != 10 or not self.phone.isdigit():
            errors.append('[Error] Phone Number must be 10 digits')

        self.email = input('Enter Your Email: ')
        if len(self.email.strip()) == 0:
            errors.append('[Error] Email cannot be empty')
        elif '@' not in self.email or '.' not in self.email:
            errors.append('[Error] Email is not valid')

        password_input = input('Enter Your Password (Min 5 Characters): ')
        if len(password_input) < 5:
            errors.append('[Error] Password must be at least 5 characters')
        else:
            self.password = hashlib.sha256(password_input.encode('utf-8')).hexdigest()

        self.address = input('Enter Your Address: ')
        if len(self.address.strip()) == 0:
            errors.append('[Error] Address cannot be empty')

        try:
            self.age = int(input('Enter Your Age: '))
            if self.age < 16:
                errors.append('[Error] Age must be 16 or older')
        except ValueError:
            errors.append('[Error] Age must be a valid number')

        # ✅ Display all errors, if any
        if errors:
            print('\n'.join(errors))
        else:
            print("[User] All inputs validated successfully.")

    def show(self):
        print('~~~~~~~~~~ {} Details ~~~~~~~~~~'.format(self.name))
        data = 'Phone: {phone} | Email: {email} | Password: {password}\nAddress: {address} | Age: {age}'.format_map(vars(self))
        print(data)

    def to_document(self):
        return vars(self)
