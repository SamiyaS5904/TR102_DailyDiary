from Day_19_8 import Visitor

visitor = Visitor()
visitor.add_visitor()
print(visitor.to_csv())

file = open('visitors.csv', 'a+')

# it checks the no of line, if no line (blank--- , it create header files)
if len(file.read()) == 0:               
    file.write('name,phone,purpose, meet_to\n') 

file.write(visitor.to_csv())