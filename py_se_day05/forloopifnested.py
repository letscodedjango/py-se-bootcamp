

dummy_string = 'This is my dummy string and seems it is gonna useful'

# when I get- i/e/n I want to print

for i in range(0, len(dummy_string)):

	if dummy_string[i] == 'i' or dummy_string[i] == 'e' or dummy_string[i] == 'n':
		print(dummy_string[i])



def print_i_e_n(text):
	dummy_string = text
	for i in range(0, len(dummy_string)):
		if dummy_string[i] == 'i' or dummy_string[i] == 'e' or dummy_string[i] == 'n':
			print(dummy_string[i])


print_i_e_n("Thsis is my test string")