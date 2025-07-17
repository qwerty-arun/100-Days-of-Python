class Employee:
	def __init__(self, role, dept, salary):
		self.role = role
		self.dept = dept
		self.salary = salary
	
	def showDetails(self):
		print("role = ", self.role)
		print("dept = ", self.dept)
		print("salary = ", self.salary)

class Engineer(Employee):
	def __init__(self, name, age):
		self.name = name
		self.age = age
		super().__init__("Engineer","IT", "75,000")

	def showDetails(self):
		super().showDetails()
		print("name = ", self.name)
		print("age = ", self.age)

eng1 = Engineer("Elon Musk", 54)
eng1.showDetails()

