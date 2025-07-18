# Searching in Objects 
#Objects of flight 
# Flight (carrier,flight_code,source, destination, departure, arrival,fare)

class Flight:
    
    def __init__(self, carrier, flight_code, source, destination, duration, departure, arrival, fare):
        self.carrier = carrier
        self.flight_code = flight_code
        self.source = source
        self.destination = destination
        self.departure = departure
        self.duration =duration
        self.arrival = arrival
        self.fare = fare

    def show(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~',self.flight_code,'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~') 
        print('Carrier : ', self.carrier)
        print('Source : ',self.source, ' | Destination : ', self.destination)        
        print('Departure : ',self.departure, ' | Arrival : ', self.arrival)
        print('Duration of Flight : ', self.duration, ' hours') 
        print('Fare : \u20b9', self.fare)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print()


flight1 = Flight(
    carrier='indigo',
    flight_code='6e642',
    source='chandigarh',
    destination='mumbai',
    departure='05:50',
    arrival='08:20',
    duration=2.3,
    fare=6499
)

flight2 = Flight(
    carrier='air india',
    flight_code='ai2660',
    source='chandigarh',
    destination='mumbai',
    departure='17:50',
    arrival='20:45',
    duration=2.5,
    fare=7260
)

flight3 = Flight(
    carrier='indigo',
    flight_code='6e5234',
    source='chandigarh',
    destination='mumbai',
    departure='16:30',
    arrival='19:05',
    duration=2.3,
    fare=7649
)

flight4 = Flight(
    carrier='air india',
    flight_code='ai522',
    source='chandigarh',
    destination='bengaluru',
    departure='16:30',
    arrival='19:30',
    duration=3.0,
    fare=6606
)


flight5 = Flight(
    carrier='indigo',
    flight_code='6e6634',
    source='chandigarh',
    destination='bengaluru',
    departure='08:25',
    arrival='11:30',
    duration=3.5,
    fare=6867
)

# List of Flight Objects
flights = [flight1, flight2, flight3, flight4, flight5]

for index in range(len(flights)):
    flights[index].show()

# Search Operation

def search_by_flight_code(flights, flight_code):
    found = False
    for flight in flights:
        if flight[index].flight_code == flight_code: 
            print("Flight Found:")
            print(flight)
            found = True
            break

    if not found:
        print("Flight code", flight_code, "not found.")

flight_code_input = input("Enter Flight Code you want to search: ")

search_by_flight_code(flights, flight_code_input)