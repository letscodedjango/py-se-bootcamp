# Dictionary 

phonebook = {}

print(phonebook)

phonebook = {
	'Andy': '9957558',
	'John': '64746484',
	'Jenny': '22282'
}

print(phonebook['Andy'])
print(phonebook['John'])
print(phonebook['Jenny'])


print(dir(phonebook))


for phone in phonebook.values():
	print(phone)

for phone in phonebook.keys():
	print(phone)

for key, value in phonebook.items():
	print(key , value)

print(phonebook)

phonebook['Mike'] = '9957558'

print(phonebook)

phonebook['Mike'] = '78474449'

print(phonebook)


print(phonebook.get('Andy'))


phonebook.update(Andy='353536735', Terry = '64547437')

print(phonebook)

update_dict = {
	'Juan': 4353536,
	'Kerry': 884747
	}

phonebook.update(update_dict)

print(phonebook)

del phonebook['Juan']

print(phonebook)




