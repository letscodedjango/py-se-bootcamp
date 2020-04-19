# One way if

# Two way - if else



# Multiway 

# 

# I have to find whether number is divisible by 6 only when the number is positive 

num = 6 

if num > 0:
	if num % 6 == 0:
		print(num)
	else:
		print('The number is not divisible by 6')
else:
	if num == 0:
		print('The number zero')
	else:
		print('Tyhe number is negative')


# 
dummy_string = 'This is my dummy string and seems it is gonna useful'

dummy_string[0]


splitted_words = dummy_string.split()



#['This', 'is', 'my', 'dummy', 'string', 'and', 'seems', 'it', 'is', 'gonna', 'useful']

print(splitted_words)

for i in range(0, len(splitted_words)):
	if splitted_words[i] == 'my' or splitted_words[i] == 'dummy' or splitted_words[i] == 'seems':
		print(splitted_words[i])










