
# words = 'This' , 'is', 'python', 'Course'

# print(words)


words = ['This' , 'is', 'python', 'Course'] # sequential manner 

print(words)


# List - ['This' , 'is', 'python', 'Course']

empty_list = []

print(empty_list)

# add some more items
# i want to remove items from list
# i want to add some items to the end of the list
# i want to add items in between to the list items
# replace 
# clear all the items 
# copy one list into list 
# reverse 


# Add 
# print(dir(empty_list))


# i want to add some items to the end of the list
empty_list.append('Python')
print(empty_list)
empty_list.append('Java')
print(empty_list)
empty_list.append('JS')
print(empty_list)

empty_list.append('Ruby')
print(empty_list)
empty_list.append('C#')
print(empty_list)
empty_list.append('JS')
print(empty_list)

empty_list.insert(1, 'Ruby')
print(empty_list)

empty_list.remove('Ruby')
print(empty_list)


another_list = empty_list.copy()

print("Before clear " , another_list)

another_list.clear()

print("After clear ", another_list)


print("Before pop " , empty_list)

empty_list.pop()

print("After pop ", empty_list)


print(len(empty_list))

for i in range(0, len(empty_list)):
	if empty_list[i] == 'Python':
		print(empty_list[i])

# Enhanced For loop

for item in empty_list: 
	print(item)

# empty_list[1]

# empty_list[-1]

print("Before sort " , empty_list)

empty_list.sort(reverse=True)

print("After sort ", empty_list)

empty_list.reverse()


print("After reverse ", empty_list)

print(empty_list)
for item in empty_list: 
	print(item)



# Tuple  - ('This' , 'is', 'python', 'Course')

names = ('John', 'Jane', 'Jenny', 'Mike')



# Set - {'This' , 'is', 'python', 'Course'}


 

# Dictionary
