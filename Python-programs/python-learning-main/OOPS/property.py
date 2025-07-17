class Student:
	def __init__(self, phy, chem, math):
		self.phy = phy
		self.chem = chem 
		self.math = math 

	#def calcPercentage(self):
		#self.percent = str((self.phy + self.chem + self.math) /3) + "%"

	@property
	def percent(self):
		return str((self.phy + self.chem + self.math) /3) + "%"

std1 = Student(98, 97, 99)
print(std1.percent)

std1.phy = 86
print(std1.percent)
