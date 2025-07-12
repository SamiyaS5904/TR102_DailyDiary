# Linked List of Flight Objects 

lass Flight:
    
    def __init__(self, carrier, flight_code, source, destination, duration, departure, arrival, fare):
        self.carrier = carrier
        self.flight_code = flight_code
        self.source = source
        self.destination = destination
        self.departure = departure
        self.duration =duration
        self.arrival = arrival
        self.fare = fare
        self.next = None
        self.previous = None

    def show(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~',self.flight_code,'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~') 
        print('Carrier : ', self.carrier)
        print('Source : ',self.source, ' | Destination : ', self.destination)        
        print('Departure : ',self.departure, ' | Arrival : ', self.arrival)
        print('Duration of Flight : ', self.duration, ' hours') 
        print('Fare : \u20b9', self.fare)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print()