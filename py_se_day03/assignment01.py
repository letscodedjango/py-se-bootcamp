# Define a function which calculate the age of any individual from current date


# born_year = 1990
# current_year = 2020
# age = current_year - born_year
# print(age)


# born_year = 1992
# current_year = 2020
# age = current_year - born_year
# print(age)


# born_year = 1998
# current_year = 2020
# age = current_year - born_year
# print(age)


# born_year = 2000
# current_year = 2020
# age = current_year - born_year
# print(age)




def calculate_age(b_year):
	born_year = b_year
	current_year = 2020
	age = current_year - born_year
	print(age)


def calculate_age(b_year):
	born_year = b_year
	current_year = 2020
	age = current_year - born_year
	print(age)


calculate_age(1992)  # 28
calculate_age(1990)  # 30
calculate_age(1998)  # 22
calculate_age(2000)  # 20


# DRY -- Do not repeat 


# Define a function which gonna convert Temperature from celcius to fahrenheit and vice versa

def convert_cel_to_far(celcius_temp):
	far_temp = (celcius_temp * 9/5) + 32
	print("The fahrenheit conversion of " + str(celcius_temp) + " is " + str(far_temp))

def convert_far_to_cel(far_temp):
	celcius_temp = (far_temp - 32) * 5/9
	print("The celcius conversion of " + str(far_temp) + " is " + str(celcius_temp))

convert_cel_to_far(100)
convert_cel_to_far(150)

convert_far_to_cel(250)
convert_far_to_cel(200)


# Define a function where you have to find whether the given number is odd or even


def find_even(number):
	is_even = number % 2 == 0
	print(is_even)
	print('The number is ' + str(number) + ' is even')

find_even(40)
find_even(39)

def find_odd(number):
	is_odd = number % 2 != 0
	print('The number is ' + str(number) + ' is odd')

find_odd(23)
find_odd(40)



