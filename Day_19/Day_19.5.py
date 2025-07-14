# PERSISITENCE : TO SAVE DATA FROM PRIMARY SOURCE TO SECONDARY (FILE/DATABASE)
    #FILE - WHEN LESS DATA 
    # DATABASE - TREE DATA STRUCTURE
  #               PROFESSIONALY SYSTEM, HIGH USE, UPDATES REQUIRED, SECURITY REQUIRED

# name = input('enter your name: ')
# person_to_meet = input('enter person name you want to meet: ')
# purpose = input('enter your purpose to meet: ')

# print('DATA: {},{},{}'.format(name, person_to_meet, purpose))

# This file read/write operation will work on plain text files
# i.e. text files (eg: .txt, .md, .py, .c, .cpp, .json etc etc)
# it wont work for docx, pdf, pptx
file = open('Day_19.py', 'r')
# data = file.read()
lines = file.readlines()
print(len(lines))
# print(lines)
# for line in lines:
#     print(line)

# Read the files, from any path of your OS Location
# file = open('/Users/ishant/Downloads/Hero-Eco-Tech.txt', 'r')
print(file.read())

file = open('D:\C C++ JCC\18.7.23 LOOPING\ap upto n terms.c', 'r')


# HW: explore how to use with keyword for file handling
#     why to use with, if we can directly access open function
# with 