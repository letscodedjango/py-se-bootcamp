#Parameter  Return

#0    0

def add_numbers1():
	no_one = 20
	no_two = 30
	result = no_one + no_two

#0    1

def add_numbers2():
	no_one = 20
	no_two = 30
	result = no_one + no_two
	return result

#1     0

def add_numbers3(x, y):
	no_one = x
	no_two = y
	result = no_one + no_two

#1     1

def add_numbers4(x, y):
	no_one = x
	no_two = y
	result = no_one + no_two
	#return result
	return result
	

output = add_numbers4(40, 50)
print(output)

