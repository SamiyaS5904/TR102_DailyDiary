# Day 5.2 - Dictionary Based Flight Booking
# Date: 20 June 2025

# Booking information using nested dictionary

one_way_flight_booking = {
    'from': {
        'location': 'Delhi',
        'description': 'DEL Delhi Airport India'
    },
    'to': 'Bengaluru',
    'traveldate': '25 June 2025',
    'travellers':  2
}

# Adding more fields later
one_way_flight_booking['returndate'] = '29 June 2025'
one_way_flight_booking['travelclass'] = 'Economy'

# Output
print(one_way_flight_booking, type(one_way_flight_booking), id(one_way_flight_booking))
