class father:
	var1 = "father"

class mother:
	var2 = "mother"

class child(father, mother):
	var3 = "I am child"
	
	def intro(self):
		print(self.var3, "of", self.var1, "and", self.var2)

ch = child()
ch.intro()
