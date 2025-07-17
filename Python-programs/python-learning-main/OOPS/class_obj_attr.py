class Student:
	college_name="ABC"
	def __init__(self, fullname):
		print("Creating a new student")
		self.name = fullname

s1 = Student("Arun")
print(s1.name)
print(s1.college_name)

s2 = Student("Logan")
print(s2.name)
print(s2.college_name)
