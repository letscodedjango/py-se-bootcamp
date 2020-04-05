# # John

# print('Take the ingredients')
# print('Mix the ingredients')
# print('Pour on pan')
# print('bake one side properly')
# print('flip dosa')
# print('Bake other side')
# print('Serve dosa to John')

# print("================")

#  # Mary
# print('Take the ingredients')
# print('Mix the ingredients')
# print('Pour on pan')
# print('bake one side properly')
# print('flip dosa')
# print('Bake other side')
# print('Serve dosa to Mary')


# print("================")
#  # Tom
# print('Take the ingredients')
# print('Mix the ingredients')
# print('Pour on pan')
# print('bake one side properly')
# print('flip dosa')
# print('Bake other side')
# print('Serve dosa to Tom')

# print("================")


# DRY - Do not Repeat Yourself 

def make_dosas(name):   # parameter variable
	print('Take the flour')
	dosa_process()  # chef
	print('Serve dosa to ' + name)


def make_masala_dosas(name):   # parameter variable
	print('Take the masala')
	dosa_process()
	print('Serve dosa to ' + name)

def make_onion_dosas(name):   # parameter variable
	print('Take the onion')
	dosa_process()
	print('Serve dosa to ' + name)

def dosa_process():  # chef
	print('Mix the ingredients')
	print('Pour on pan')
	print('bake one side properly')
	print('flip dosa')
	print('Bake other side')


make_dosas('John')

print("================")

make_dosas('Mary')

print("================")

make_dosas('Tom')


















