class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(self.length * self.breadth)
    
    def perimeter(self):
        print((self.length + self.breadth) * 2)

rec1 = Rectangle(1, 2)
rec1.area()
rec1.perimeter()