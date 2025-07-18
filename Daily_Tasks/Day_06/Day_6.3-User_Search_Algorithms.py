# Linear search using both while and for loops

usernames = ['john', 'jennie', 'fionna', 'kia', 'leo']
search = input('Enter username to search: ')

# While loop search
index = 0
flag = False
while index < len(usernames):
    if usernames[index] == search:
        print('User Found at index', index)
        flag = True
        break
    index += 1

if not flag:
    print('User Not Found (while loop)')

# For loop search
flag = False
for index in range(len(usernames)):
    if usernames[index] == search:
        print('User Found at index', index)
        flag = True
        break

if not flag:
    print('User Not Found (for loop)')

