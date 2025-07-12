"""
Single Vlue containers (which hold 1 value)
    int, float, bool

Multi Value Containers (which hold lot of data)
    objects -> tuple, list, string, set, dictionary

Sequences
    Tuple
    list
    string

    storage of data is sequential or linear

    storage of data is non sequential or non linear
    set 
    dictionary

    Properties:
    1. Indexing
    2. Negative Indexing
    3. Slicing
    4. Concatenation
    5. Multiplicity
    6. Membership Testing   

Negative indices count from the end:

-1 → last element

-2 → second last, and so on.


"""


# LIST
#1D List                       D ----> Dimension
my_data = (10,20,30)
print('my_data[0]: ',my_data[0])

#List of Lists
# 2D List
# 2D Lists shows images (Black and White)
numbers = [
            [10,20,30],       # 0 index
            [40,50,60],       # 1 index
            [70,80,90,100],   # 2 index
]
print('numbers[0]: ',numbers[0])
print('numbers[0][2]: ',numbers[0][2])     # it goes to 2nd index of 0th index 
print('Length of numbers: ', len(numbers))
print('numbers[-1]',numbers[-1])
print('numbers[-2]',numbers[-2])
print('numbers[-3]',numbers[-3])

#3D representation (Used in colored images)
#List of List of List 
large_data = [
                [
                #  -3   -2  -1
                #    0   1  2
                    [10,20,30],         #0
                    [40,50,60],         #1          #0 -2
                    [70,80,90],         #2
                ],
                [
                    [10,20,30],         #0
                    [40,50,60],         #1          #1 -1
                    [70,80,90],         #2
                ]
]
print('Length of large_data: ', len(large_data))    # it wil be 2 only as we have 2 lists inside list
# In python we can use n dimensional representation of data
# A * A INVERSE = I (used in Encryption Decryption Technique)

print('large_data[-1][-2][-2]',large_data[-1][-2][-2])



# name ="Johns Cafe"
# name = 'John\'s Cafe'

message = """This is Awesome
Welcome to Johns Cafe
    You get happiness with good food here """

print('message')
print(message)

print("Length of message", len(message))
print("message[1] is: ", message[1])
print("message[-4] is: ", message[-4])

print("message[len(message)-1] is :",message[len(message)-1])
print("message[-len(message)] is :",message[-len(message)])


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# Property 3. SLICING   (works as subsets, not mathematically)
   # to get some part of string as new string from a big string 
# SLICE FUNCTION -> if we want steps, we can explore slice as built in in python

""" range(10, 101, 10) means:
Start from 10
Go up to 100 (because range stops before 101)
Increase by 10 each time.
         -10  -9  -8  -7  -6  -5  -4  -3  -2   -1
# data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
"""

data = list(range(10,101,10))
print('data: ', data)

print(data[0:3])     #it picks the elements starting from 0 till 2 i.e, less than 3
print(data[3:7])     # from 3 to 6
print(data[5:])      # from 5 till end
print(data[:4])      # from 0 to 3

print(data[-5:-2])  # 60,70,80     -2 is not included
print(data[ : -5])  # 10,20,30,40,50


email = 'john@example.com'

name = email[:4]     #john
domain =email[5:]    #example.com
print('name: ', name)
print('domain: ', domain)

# Slicing Real time usage in strings

# Property 4 : Concatenation
# sllicing, concatenation both make new string in memory

data1 = [10,20,30]
data2 = [50,70,90]

data3 = data1 + data2

print('data3 : ', data3)

# Concatentaion on Tuple (same operations as lists)
data1 = (10,20,30)
data2 = (50,70,90)

data3 = data1 + data2      
print('data3 :', data3)


# Concatenation on String
salutation = 'Mr.'
full_name = 'John Watson'

name = salutation + full_name 
print('name: ', name)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# Property 5 : MULTIPLICITY 
dataaa = [10,30,80,-4,-198]
data4 = dataaa*3
print('data4 : ', data4)

# Real Time usage of Multiplicity ----> 

# 6. Membership Testing
print("10 in dataaa",10 in dataaa)
print("exam in email:", 'exam' in email)
print("hello not in email :", 'hello' not in email)


# Real Time usage of Membership Testing ----> 













