name = 'Howard Mwangi'
age = '25'
location = 'Nairobi'
school = 'KU'
job = 'TechCamp'

# we use square brackets to tell python its a list
Person1 = ["Howard Mwangi",25, "Nairobi", "KU", "TechCamp"]

# we use indexing to access various items in a list

front_row_students = ['Said', 'Howard', 'Najib', 'Anne', 'Peter']
first = front_row_students[0]
Last = front_row_students [-1]
print(first)
print(Last)

# How do you get the first say 100 students
# This is a range
first2 = front_row_students [0:2]
print(first2)
# This is called list slicing - The integer left of the colon is the first value in the list
# the integer right of the colon is normally the last list item but its exclusive meaning not taken

# LIST OPERATIONS
    # 1. concatenating a list
form1east = ['Howard']
form1west = ['Melvin']
form1 = form1east + form1west
print(form1)
print(len(form1))
# len is a function used to count the number of variables in a list

# Determining Membership in a list
# in is reserved to check for membership in a list
is_melvin = 'Melvin' in form1
print(is_melvin)

# assignment
# list methods
# form1.
# know what each and every one of the methods does
# especially append, extend, pop