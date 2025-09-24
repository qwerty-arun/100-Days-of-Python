class Student:
    def __init__(self, name, roll, *marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    
    def avg(self):
        return sum(self.marks) / len(self.marks)
    
    def grade(self):
        if self.avg() > 90:
            print("A")
        elif 75 <= self.avg() < 90:
            print("B") 
        else:
            print("C")

std = Student("Arun", 12, 34, 56, 100, 100)
print(std.avg())
std.grade()