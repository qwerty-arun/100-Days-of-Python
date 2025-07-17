class Student:
	def __init__(self, fullname):
		print("Creating a new student")
		self.name = fullname

s1 = Student("Arun")
print(s1.name)
