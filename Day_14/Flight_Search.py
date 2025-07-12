# Flight Dictionary Data (same as yours)

flight_1 = {
    'carrier': 'indigo',
    'flight_code': '6e2069',
    'from': 'chandigarh',
    'to': 'bengaluru',
    'duration': '2.45',
    'departure': '5:45',
    'arrival': '8:00',
    'fare': '6525'
}

flight_2 = {
    'carrier': 'air india express',
    'flight_code': 'ix2508',
    'from': 'delhi',
    'to': 'bengaluru',
    'duration': '3',
    'departure': '5:00',
    'arrival': '8:00',
    'fare': '6626'
}

flight_3 = {
    'carrier': 'indigo',
    'flight_code': '6e2103',
    'from': 'delhi',
    'to': 'bengaluru',
    'duration': '2.55',
    'departure': '7:00',
    'arrival': '9:55',
    'fare': '6810'
}

flight_4 = {
    'carrier': 'spice_jet',
    'flight_code': 'sg11',
    'from': 'delhi',
    'to': 'dubai',
    'duration': '3.40',
    'departure': '8:00',
    'arrival': '10:10',
    'fare': '10596'
}

flight_5 = {
    'carrier': 'air_india',
    'flight_code': 'ai2209',
    'from': 'delhi',
    'to': 'dubai',
    'duration': '3.45',
    'departure': '20:30',
    'arrival': '22:45',
    'fare': '11251'
}

# List of Dictionaries
flights = [flight_1, flight_2, flight_3, flight_4, flight_5]

# ✅ Function to Search by Flight Code
def search_by_flight_code(flights, flight_code):
    found = False
    for flight in flights:
        if flight['flight_code'].lower() == flight_code.lower():  # case-insensitive match
            print("Flight Found:")
            print(flight)
            found = True
            break

    if not found:
        print("Flight code", flight_code, "not found.")

flight_code_input = input("Enter Flight Code you want to search: ")

search_by_flight_code(flights, flight_code_input)
