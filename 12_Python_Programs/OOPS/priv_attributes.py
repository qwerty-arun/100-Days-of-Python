class Account:
	def __init__(self, acc_no, acc_pass):
		self.acc_no = acc_no
		self.__acc_pass = acc_pass
	
	def reset_pass(self, new_pass):
		self.__acc_pass = new_pass
	
	def display_pass(self):
		print(self.__acc_pass)


acc1 = Account("12345", "password")
print(acc1.acc_no)
acc1.reset_pass("newpassword")
acc1.display_pass()
