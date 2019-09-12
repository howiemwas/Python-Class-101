# Dictionary holds key and value pairs

person1 = ['Howard', 25, 'Nairobi', 'KU', 'TechCamp']

# this is a number
a = 0

# this is a string ''
b = ''

# this is a list
c = []

# this is a tuple
d = ()

# this is a dictionary
e = {'name':'Howard', 'phonenumber':'0726619088', 'age':'25', 'location':'Nairobi', 'University':'KU',
     'Instructor':'Techccamp', 'marks':{'math':32,'english':45,'History':67,'Civics':89},
    'dateofbirth':(24,'Dec',{'born':1994, 'born again':2005})}

print(e['name'])

print(e['marks']['math'])

print(e['dateofbirth'])
print(e['dateofbirth'][2]['born again'])

e.clear()
print(e)

del e
print(e)
