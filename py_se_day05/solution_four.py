# Define a function that helps to calculate the area of circle with different radius and print the area only when the area is divisible by 4

# 23.48, 56.78, 45.67, 78.28 Please consider the unit of these values as cm



def calculate_area(radius):
	PI = 3.14
	area = PI * radius * radius
	if area % 6 != 0:
		print('The area of circle with radius {0} is {1}'.format(radius, area))


def calculate_square(num):
	squared = num * num
	if num % 2 != 0:
		new_num = squared + num
		print(new_num)
	print(squared)


# Define a function using Python that helps to find the first five character of string in all the possible ways

string = HAPPY CODING

string[9:len(string)]

string[9:]

string[-3:]

# Define a function using Python that helps to find the last 3 character of string in all the possible ways


for i in range(5, 51):
	print(1)


i = 5
while i <= 50:
	print(i)
	i = i + 5

#Design a function that accept 6 values & find the average of those values which are only divisible by 6.

def calculate_average(n1, n2, n3, n4):
	sum = 0
	count = 0

	if n1 % 6 == 0:
		sum = sum + n1  # n1=6
		count = count + 1

	if n2 % 6 == 0:
		sum = sum + n2  # n1 = 12
		count = count + 1

	if n3 % 6 == 0:
		sum = sum + n3  # n3 = 4
		count = count + 1

	if n4 % 6 == 0:
		sum = sum + n4 # n4= 18
		count = count + 1

    avg = sum / count

    print(avg)
	





