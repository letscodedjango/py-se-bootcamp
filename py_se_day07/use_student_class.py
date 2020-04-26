from pysebootcamp.py_se_day07 import student_module
from pysebootcamp.py_se_day07.student_module import Student

# john = student_module.Student("John", 26, "B.E", 13244, "john@gmale.com", 1, "Python")
# mike = student_module.Student("Mike", 27, "B.E", 34353, 2, "Java")
# jenny = student_module.Student("Jenny", 23, "B.E", 758597, 3, "JavaScript", email="jenny@gmale.com")
# ramu = student_module.Student("Ramu", 26, "Ph.D", 343536, "rambo@gmale.com", 4, "Python")

john = Student("John", 26, "B.E", 13244, "john@gmale.com", 1, "Python")
mike = Student("Mike", 27, "B.E", 34353, 2, "Java")
jenny = Student("Jenny", 23, "B.E", 758597, 3, "JavaScript", email="jenny@gmale.com")
ramu = Student("Ramu", 26, "Ph.D", 343536, "rambo@gmale.com", 4, "Python")

print(john.name)
print(mike.name)
print(mike.name)