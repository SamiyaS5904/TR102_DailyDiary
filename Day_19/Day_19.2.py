# Creating a dictionary with list, having keys as elements of list

months_list = ['jan', 'feb', 'mar',
               'apr', 'may', 'june',
               'july', 'aug', 'sep',
               'oct', 'nov', 'dec']

college_attendence = {}.fromkeys(months_list, 100)

print('college_attendence')
print(college_attendence)

college_attendence['jan'] -= 5

print('college_attendence')
print(college_attendence)


print('~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 10 students -- each students each month attendence by deafult 100

my_data ={
    205 : 'samiya',
    208 : 'savreet',
    220 : 'simran kaur',
    221 : 'simran',
}

keys = list(my_data.keys())
values = list(my_data.values())

print(keys)
print(values)

