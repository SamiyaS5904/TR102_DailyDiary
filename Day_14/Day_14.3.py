# Searching in Dictionary

# Flight Dictionary

flight_1  ={

    'carrier' : 'indigo',
    'flight_code' : '6e2069',
    'from' : 'chandigarh',
    'to' : 'bengaluru',
    'duration' : '2.45',
    'departure' : '5:45',
    'arrival' : '8:00',
    'fare' : '6525'
}

flight_2 = {

    'carrier' : 'air india express',
    'flight_code' : 'ix2508',
    'from' : 'delhi',
    'to' : 'bengaluru',
    'duration' : '3',
    'departure' : '5:00',
    'arrival' : '8:00',
    'fare' : '6626'
}

flight_3 = {

    'carrier' : 'indigo',
    'flight_code' : '6e2103',
    'from' : 'delhi',
    'to' : 'bengaluru',
    'duration' : '2.55',
    'departure' : '7:00',
    'arrival' : '9:55',
    'fare' : '6810'
}

flight_4 = {

    'carrier' : 'spice_jet',
    'flight_code' : 'sg11',
    'from' : 'delhi',
    'to' : 'dubai',
    'duration' : '3.40',
    'departure' : '8:00',
    'arrival' : '10:10',
    'fare' : '10596'
}

flight_5 = {

    'carrier' : 'air_india',
    'flight_code' : 'ai2209',
    'from' : 'delhi',
    'to' : 'dubai',
    'duration' : '3.45',
    'departure' : '20:30',
    'arrival' : '22:45',
    'fare' : '11251'
}

# List of Dictionary Objects
flights = [flight_1, flight_2, flight_3, flight_4, flight_5]

# Use Linear Search, to search flights from chandigarh to mumbai or begaluru

# Filter Says: Search all of the data/elements matching criteria

"""
source = input('Enter Source Location')
destinition = input('Enter Destinition Location')

# Filtering
for index in range(len(flights)):

    if flights[index]['from'] == source and flights[index]['to'] == destinition:
        print(flights[index])
"""

# Search Operation
def search(flights, element=None):
    flag = False
    for index in range(len(flights)):
        if flights[index] == element:
            print(flight_code, 'Flight is available')
    
            flag = True
            break

    if flag == False:
        print(element, 'Element not found')


flight_to_search = int(input('Enter flight Number you want to search: '))
search(flights, flight_to_search)

   
    