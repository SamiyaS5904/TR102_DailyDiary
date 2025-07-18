# Program 3. Making a search function

def search(data, element=None):  # ✅ Incorrect syntax in your code was 'data[]'
    flag = False
    for index in range(len(data)):
        if data[index] == element:
            print(element, 'Found at index:', index)
            flag = True
            break

    # This should be outside the loop, and no need to check inside the loop
    if flag == False:
        print(element, 'Element not found')

# Example lists
names = ['john', 'jennie', 'anna', 'kim', 'ben']
data = [10, 20, 30, 40, 50]

element_to_search = int(input('Enter which Number you want to search: '))
search(data, element_to_search)

search(names, 'ben')
search(names, 'kia')
