class Car:
	def __init__(self, type):
		self.type = type

	@staticmethod
	def start():
		print("car started")
	
	@staticmethod
	def stop():
		print("car stopped")
	
class Toyota(Car):
	def __init__(self, name, type):
		# comment the below line to see the effect
		super().__init__(type)
		self.name = name
	
car = Toyota("prius", "electric")
print(car.type)
