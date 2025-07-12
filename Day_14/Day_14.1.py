# Program 2. Searching Names in a list 
# Searching names

names = ['john', 'jennie', 'anna', 'kim', 'ben']
name = input('Enter Name to Search : ')
index = 0
found = 0 

while index < len(names):
    if names[index]==name:
        print('Name found at :', index)
        found = 1
        break

   index = index + 1
     
     if found == 0
    print ('Name not Found')
