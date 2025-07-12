"""
Assignment : Shopping Cart as a Circular Doubly Linked List
    Amazon/ any Ecommerce application -- zomato/blinkit --
"""

# Product has quantity and Price as 2 important attributes

# Circular Doubly LL
# a function is to be made where we will be deleting / adding objects (Updating quantity)
# if quantity is updated as 0 -> delete from list 

# Level 2 :
# Searching -> 
# sorting -> price/ quantity high to low or low to high
# filter ->
# Apply promocode function -- give any suitable discounts

class Product:

    def __init__(self, name='', category='', quantity='0', price='', brand='', product_id=''):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.brand = brand
        self.next = None
        self.previous = None

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('Name:', self.name)
        print('Category:', self.category)
        print('Quantity:', self.quantity)
        print('Price:', self.price)
        print('Brand:', self.brand)
        print('Product_ID:', self.product_id)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
