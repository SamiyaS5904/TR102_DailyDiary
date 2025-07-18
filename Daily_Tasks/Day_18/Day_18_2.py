numbers = list(range(10,101,10))
print('numbers : ', numbers)

print(id(numbers))
print(hex(id(numbers)))

# APPEND -> add numbers at the end
# append is the inbuilt function of LIST
# when dot operators used, check ke vo kiska function hai 

numbers.append(99)
numbers.append(43)
numbers.append(32)
numbers.append(-99)

print()
print('~~~~~~~~~~~~`INBUILT PYTHON FUNCTIONS~~~~~~~~~~~')
print('numbers :', numbers)
print('Length of numbers :',len(numbers))
print('Sum of numbers :',sum(numbers))
print('Minimum of numbers :',min(numbers))
print('Maximum of numbers :',max(numbers))
print('Average of numbers :',sum(numbers)/len(numbers))
print('Average of numbers :',int(sum(numbers)/len(numbers)))

data=tuple(numbers)
print('data is :', data)

#data.append(30) # error 
# tuple can't be updated

# Reverse functions can't be done directly 
reverse_numbers =list(reversed(numbers))
print('reverse_numbers: ', reverse_numbers)


idx = numbers.index(40)
print('idx is :', idx)

data = [10,30,50,20,5,30,15]
names = ['john', 'abel', 'sia', 'kim', 'anna', 'joe']

data.sort()
print('Sorted data : ', data)

print()

names.sort()            # names are sorted on basis of their ASCII values
print('Sorted names : ', names)

# Remove -> to remove data from lists 
# data is removed from beginning -- jhan mil jayega vhan se hatadega
data.remove(30)
data.remove(15)
names.remove('abel')

print('Data Now : ', data)
print('Names Now : ', names)


# List as STACK
data = [10,20,30,40,50,60,70]
print('data : ', data)

# pop 1
data.pop()    
print('data aftter pop 1 :', data)  

# pop 2
data.pop(0)                
print('data aftter pop 2 :', data)

data.clear()
print('Data after clear : ', data)

data = [10,20,30,40,50,60]
data.insert(2,77)   # insert 77 at 2 nd index
data.insert(-1,88)  # it insert 88 at second last position

# Python Functions (where we don't use dot (.) operators)
# del data[1]

# tuple ----> no Modifications can be there --- so no functions can be used !!! :)


