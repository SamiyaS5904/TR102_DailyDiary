# Sorting

 # Sequence / Arrangement of data 

# Bubble sort

"""
    -> 2 numbers are compared 
    -> after each pass, the largest number comes at the last -----
"""
data = [50,40,30,20,10]

for comparisons in range (0, len(data) - 1):

    for index in range (len(data) - comparisons - 1):

        if data[index] > data[index + 1]:
            temp = data [index]
            data [index] = data [index + 1]
            data [index + 1]=temp

        index = index - 1  
       
print ('Ascending Sorting of data', data)   