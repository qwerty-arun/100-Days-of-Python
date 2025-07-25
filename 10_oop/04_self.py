# Self Argument

class Chaicup:
    size = 150 #ml

    def describe(self):
        return f"A {self.size} ml chai cup"

cup1 = Chaicup()
print(cup1.describe())
print(Chaicup.describe()) # error
print(Chaicup.describe(cup1)) # no error