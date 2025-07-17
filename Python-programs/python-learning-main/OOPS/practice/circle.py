class Circle:
	def __init__(self, r):
		self.r = r
	
	def Area(self):
		print("Area: ", 3.1415 * self.r ** 2)

	def Perimeter(self):
		print("Perimeter: ", 2 * 3.1415 * self.r)
	
c1 = Circle(1)
c1.Area()
c1.Perimeter()
