# class CircularDoublyLinkedList

class Shopping_Cart:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, product):
        self.size += 1
    
        if self.head == None:
            self.head = product
            self.tail = product
            

        else:
            self.tail.next = product
            product.previous = self.tail
            product.next = self.head
            self.head.previous = product
            self.tail = product