# 
def add_numbers():
	no_one = 20
	no_two = 30
	result = no_one + no_two
	print(result)

# add_numbers()

def add_numbers_version_01(x, y):
	no_one = x
	no_two = y
	result = no_one + no_two
	#print("The value of result variable is " +  str(result) ) ### ?
	return result
	
	# print(result)

# x = add_numbers_version_01(20,30)
# print(x)  # ?

	# not returning anything to you 

# add_numbers_version_01(50, 10)
# add_numbers_version_01(300, 29)
# add_numbers_version_01(20.78, 56.89)


# # Average of two numbers 
# Add 2 nos and then divide the sum with nos. of value 

# no_one = 50 
# no_two = 60 
# nos_sum = no_one + no_two

# nos_sum = add_numbers_version_01(50, 50)   ### This particular line of code will throw error

# avg  = nos_sum/2  # 50.0

# print(avg)  ## 

# nos_sum = add_numbers_version_01(40, 50)   ### This particular line of code will throw error

# avg  = nos_sum/2  # 50.0

# print(avg)  ## 


# nos_sum = add_numbers_version_01(140, 150)   ### This particular line of code will throw error

# avg  = nos_sum/2  # 50.0

# print(avg)  ## 



def calculate_avg_of_two_numbers():
	nos_sum = add_numbers_version_01(50, 50) 
	avg  = nos_sum/2  # 50.0
	return avg

output = calculate_avg_of_two_numbers()
print(output)


def calculate_avg_of_two_numbers_version_02(x, y):
	nos_sum = add_numbers_version_01(50, 50)
	avg  = nos_sum/2  # 50.0
	return avg



def calculate_avg_of_two_numbers_version_01(x, y):
	nos_sum = add_numbers_version_01(x, y) 
	avg  = nos_sum/2  # 50.0
	return avg


output = calculate_avg_of_two_numbers_version_01(30, 30)
print(output)

output = calculate_avg_of_two_numbers_version_01(40, 50)
print(output)

output = calculate_avg_of_two_numbers_version_01(140, 150)
print(output)

output = calculate_avg_of_two_numbers_version_01(230, 30)
print(output)



