names = ('John', 'Jane', 'Jenny', 'Mike', 'Jane')

names = ()

# print(names[0])

# for name in names:
# 	print(name)

# print(dir(names))

# print(names.index('Jane'))

# immutable - 
# mutable - which can be changes 

# print(names.count('Jane'))

# print(names)

# Set 
set_names = {'John', 'Jane', 'Jenny', 'Mike', 'Jane'}

print(set_names)

print(dir(set_names))

set_names.add('Jackson')

print(set_names)

set_names.add('Mike Tyson')

print(set_names)

for name in set_names:
	print(name)



copy_set = set_names.copy()
print(copy_set)

copy_set.clear()
print(copy_set)

empty_set = set()
print(empty_set)

empty_set.add('Orange')
print(empty_set)


set_names = {'John', 'Jane', 'Jenny', 'Mike', 'Jane'} # superset

new_set = {'John', 'Jane', 'Andy'}  # subset


is_subset = new_set.issubset(set_names)
print(is_subset)

is_intersection = new_set.intersection(set_names)
print(is_intersection)

is_intersection = new_set.difference(set_names)
print(is_intersection)

is_intersection = set_names.difference(new_set)
print(is_intersection)



# set_names.remove('Jackson')
# print(set_names)

set_names.discard('Jackson')
print(set_names)











