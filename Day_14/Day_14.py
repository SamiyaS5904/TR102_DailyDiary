# Search 
# Sort 
# Filter

# 1. using simple list
# 2. using Dictonary (list of Dictionary)
# 3. Objects (List of Objects)
# 4. Linked List

"""
#### SEARCH, SORT, FILTER ALGORITHMS CAN ONLY BE APPLIED ON HOMOGENEOUS DATA 

1. Search - 
    a. Linear Search -
            - Time consuming (if element is present at last)
    b. Binary Search - 
            - using prev, mid, next --- (like dividing in 2 parts and then working)

        ## Linear Search
        # 1. In simple list
        # 2. in List of Dictionary
        # 3. List of objects
        # 4. Our LL      
"""
# Program 1. Searching Numbers in a list 
# TIME COMPLEXITY OF LINEAR SEARCH ---> O(N)

from enum import Flag
data = [10,20,30,40,50]

number = int(input('Enter number to search :')) 

for index in range(len(data)):
    if data[index]== number:
        print('Number found at index :',index)
        Flag == True
        break

if Flag == False :
    print('Number not Found')