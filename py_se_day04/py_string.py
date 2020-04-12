## To define string

random_string = 'This is a session on python'

another_string = "Its awesome to be here with you all"

new_string_one = "It's awesome to be here with you all"

new_string = 'It\'s awesome to be here with you all'

new_string_two = "It\"s awesome to be here with you all"

# print(new_string)

# print(new_string_two)

new_string_two = "HELLO Guys !!"

# To find the length of string
len(new_string_two)



print(len(new_string_two))

# # To access O
print(new_string_two[4])

# Slicing of string
print(new_string_two[0:4])   # including 0 excluding 4

print(new_string_two[2:13])

print(new_string_two[2:len(new_string_two)])

print(new_string_two[2:])

print(new_string_two[:5])


print(new_string_two[-4:-1])

# print(new_string_two[-1:-4])

# Changes the cases -

new_string_two = "HELLO Guys !!"

new_string_title = "hELLO guys !!"

print(new_string_two.lower())
print(new_string_two.upper())
print(new_string_title.title())  ## it will convert the first letter of every word within any string in upper case
print(new_string_title.capitalize())  # it will convert the first letter of any string in upper case


# 

hi_string = new_string_title.replace('Hi', 'Hello')
print(hi_string)

#
L_count = new_string_title.count('L') 
print(L_count)
l_count = new_string_title.count('l')
print(l_count)


# 
name_list = "Mr. John Doe"

split_string = name_list.split()
print(split_string)

split_string = name_list.split('.')
print(split_string)


# 
space_string = 'John Doe'
print(len(space_string)) # 8

space_string_two = ' John Doe '
print(len(space_string_two)) # 10

space_string_strip = space_string_two.strip()
print(len(space_string_strip))


#
#print(dir(space_string_strip))

# 

print(space_string.find('Doe')) # 0 - 14

print(space_string.find('z'))


# 
print(space_string.index('J'))
print(space_string.index('Doe'))

print(space_string[:-1])

print(space_string)





