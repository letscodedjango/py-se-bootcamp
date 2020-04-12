# Define a function that helps to calculate the area of circle with different radius
#   `23.45, 56.78, 45.67, 78.9`



def calculate_area_of_circle(radius):
	PI = 3.14
	result = PI * radius * radius
	return result


output = calculate_area_of_circle(23.45)
print(output)
output = calculate_area_of_circle(56.78)
print(output)
output = calculate_area_of_circle(45.67)
print(output)
output = calculate_area_of_circle(78.9)
print(output)


def find_last_and_first_char(text):
	first_char = text[0]
	last_char = text[-1]
	print(first_char + ' - ' + last_char)
	return first_char,last_char

find_last_and_first_char("This is python class")
find_last_and_first_char("Its awesome to be here")


#Define a function that helps to find the square of any number and then add the same number to the squared number and return the final output.

def calculate_square_and_add(number):
	square = number * number
	result = square + number
	return result


output = calculate_square_and_add(6)
print(output)
output = calculate_square_and_add(10)
print(output)




