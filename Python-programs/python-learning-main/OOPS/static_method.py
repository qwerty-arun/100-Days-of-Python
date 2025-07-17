class Student:
	college_name="ABC"
	def __init__(self, fullname, marks):
		self.name = fullname
		self.marks = marks
	def average(self):
		sum = 0
		for mark in self.marks:
			sum = sum + mark
		print("Average:",sum/3.0)
	
	@staticmethod
	def hello():
		print("Hello")
		

s1 = Student("Arun", [90, 100, 100])
print(s1.name)
print(s1.college_name)
s1.average()
s1.hello()
