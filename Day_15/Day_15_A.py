def sort(data, low_to_high=0):

    if low_to_high ==0:

        for outer in range(len(numbers)-1):
            for inner in range(len(numbers)-outer-1):
        
                if numbers[inner] > numbers[inner+1]:
                    temp = numbers[inner]
                    numbers[inner] = numbers[inner+1]
                    numbers[inner+1] = temp

    if low_to_high ==1:
        for outer in range(len(numbers)-1):
            for inner in range(len(numbers)-outer-1):
        
                if numbers[inner] < numbers[inner+1]:
                    temp = numbers[inner]
                    numbers[inner] = numbers[inner+1]
                    numbers[inner+1] = temp

numbers = [10,68,8,23,11,-43,0,100]
sort(data=numbers)
print(numbers)

## We can also sort strings instead of numbers ----------->

names = ['john', 'sia', 'kim', 'anna', 'ben','tom']
sort(data=names)
print('Sorted Names : ', names)