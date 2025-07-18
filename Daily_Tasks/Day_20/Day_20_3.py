## VIEW -------- (MVC)

"""
APPLICATION
"""
from Day_20_1 import Visitor
from Day_20_2 import FileHelper

class VisitorApp:

    def __init__(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("Welcome to Visitor Log Book App")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # Create a File Helper Object

        # VisitorApp has file_helper ---------
        self.file_helper = FileHelper()                                               # It calls to init function, when class name is called with ()

    def show_menu(self):
        
        while True:
            print('~~~~~~~~~~Select Option~~~~~~~~~~')
            print("1: Log a Visit")
            print("2: View Visit Log Book")
            print("3: Quit")
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            choice = int(input('Enter Your Choice: '))


           
            if choice == 1:
                self.add_visitor()
            elif choice == 2:
                self.view_all_visitors()
            elif choice == 3:
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print('Thank You for Using Visitor App')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                break
            else:
                print("Invalid Menu Option")

    def add_visitor(shelf):
        # 1. Create an empty visitor object
        visitor = Visitor()

        # 2. input details 
        visitor.input_visitor_details()

        # 3. save visitor in file
        visitor.serial_no = self.file_helper.lines_in_file()

        self.file_helper.write_in_file(content=str(visitor))


    def view_all_visitors(self):
        self.file_helper.read_file()

