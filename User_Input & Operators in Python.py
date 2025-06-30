# Day 5.3 - User Input and Python Operators
# Date: 20 June 2025

# Collecting user input for booking
from_location = input('Enter From Location: ')
travelers = int(input('Enter Number Of Travelers: '))
feedback = float(input('Enter Your Feedback (1-5): '))

flight_booking = {
    'from': from_location,
    'travelers': travelers,
    'feedback': feedback
}

print(flight_booking, type(flight_booking))

# ---------------------------------------------
# Arithmetic Operators Example

cab_fare = 1000
taxes = 0.18
tax_to_pay = cab_fare * taxes
amount_to_pay = cab_fare + tax_to_pay

print('Tax to Pay:', tax_to_pay)
print('Total Amount:', amount_to_pay)

# ---------------------------------------------
# Conditional Operators

e_wallet = 1000
can_cab_be_booked = e_wallet >= cab_fare
print("Can cab be booked:", can_cab_be_booked)

# ---------------------------------------------
# Logical Operators

internet = True
gps = True
google_maps_access = internet and gps
print("Google Maps Access:", google_maps_access)

# ---------------------------------------------
# Assignment Operators

number = 10
number += 1
number *= 2
print('Updated number:', number)

# ---------------------------------------------
# Bitwise Operators

number1 = 10  # 1010
number2 = 8   # 1000
result = number1 | number2  # 1010
print("Bitwise OR Result:", result, bin(result))
