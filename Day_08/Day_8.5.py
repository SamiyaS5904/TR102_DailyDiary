def square_of_numbers(numbers):
    print('[square_of_numbers] numbers is: ', numbers, id(numbers), type(numbers))
   
    for index in range(len(numbers)):
        print('[square_of_numbers]', numbers[index], type(numbers[index]), id(numbers[index]))
    for index in range(len(numbers)):