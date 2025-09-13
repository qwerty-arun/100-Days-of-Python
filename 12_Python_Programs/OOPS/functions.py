class Student:
	college_name="ABC"
	def __init__(self, fullname):
		print("Creating a new student")
		self.name = fullname
	def hello(self):
		print("welcome", self.name)

s1 = Student("Arun")
print(s1.name)
print(s1.college_name)
s1.hello()
