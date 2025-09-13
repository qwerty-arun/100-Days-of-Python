class Complex:
	def __init__(self, real, imag):
		self.real = real
		self.imag = imag

	def showNumber(self):
		print(self.real, "+", self.imag, "* j")

	# Dunder function
	def __add__(self, num2): 
		newReal = self.real + num2.real
		newImag = self.imag + num2.imag
		return Complex(newReal, newImag)

	def __sub__(self, num2): 
		newReal = self.real - num2.real
		newImag = self.imag - num2.imag
		return Complex(newReal, newImag)

num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(3,-9)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

num4 = num1 - num2
num4.showNumber()
