# Circular Doubly LL

class FlightList:
       def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, song):
        self.size += 1

        if self.head == None:
            self.head = song
            self.tail = song
            
        else:
            self.tail.next = song
            song.previous = self.tail
            song.next = self.head
            self.head.previous = song
            self.tail = song