# # strings are enclosed in quotation or speech marks
# # this is to tell python that take that value literally
# # strings are also called literals
# name = 'Howard Mwangi + Letina'
#
# marks = 45+40
# mark = '45+40'
# print(name)
#
# # Phone numbers are often put in quotations
# phone_number = '070627777777'
# print(type(phone_number))
#
#
# print(type(phone_number))
#
# # typecasting
# phone_number = int(phone_number)
# print(phone_number)
# print(type(phone_number))
#
# phone_number = str(phone_number)
# print(type(phone_number))

# String operations
# we use a plus sign to concatenate strings
first_name = 'said'
second_name = 'Najib'
full_name = first_name + " " + second_name
print(full_name)

first_name = 'said '
second_name = 'Najib'
full_name = first_name + second_name
full_name = first_name + second_name
print(full_name)
print(first_name.title())
print(first_name.upper())
print(full_name.split())
print(first_name.count('a'))


gender = "MFMFMFMFMFMFMFMFMFMFMFMFMFMF"
print(gender.count('F'))
print(gender.count('M'))

# assignment
# list methods
# form1.
# know what each and every one of the methods does
# especially append, extend, pop

animalList = ['Cow','Donkey', 'Goat', 'Monkey', 'Zebra']
print(animalList)
print(animalList.append(1, 'Dog'))