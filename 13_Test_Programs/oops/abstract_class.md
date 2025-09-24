# Abstract Classes
- In Python, **abstract classes** are classes that **cannot be instantiated directly** and are meant to serve as **blueprints** for other classes. They are useful when you want to enforce that certain methods **must** be implemented in any subclass.

---

### 🔑 Key Points:

1. Defined using the `abc` (Abstract Base Class) module.
2. Use the `ABC` class from `abc` as a base.
3. Use the `@abstractmethod` decorator to mark methods that must be implemented in subclasses.
4. Subclasses of an abstract class must override all abstract methods, otherwise they will also be abstract (cannot be instantiated).

---

### ✅ Example

```python
from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass


# Concrete subclass
class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


# Using the class
rect = Rectangle(10, 5)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())
```

👉 If you try to do `shape = Shape()`, you’ll get an error:

```
TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter
```

---

### ⚡ Extra Features

* Abstract classes can have **normal (concrete) methods** too.
* They can have **instance variables** and **constructors**.
* You can define **abstract properties** with `@property` and `@abstractmethod`.

---

### Example with Abstract Property

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @property
    @abstractmethod
    def wheels(self):
        pass

class Car(Vehicle):
    @property
    def wheels(self):
        return 4

mycar = Car()
print(mycar.wheels)  # 4
```

---

⚖️ **When to use abstract classes?**

* When you want to enforce a consistent interface across subclasses.
* When some methods are **mandatory** for child classes to implement.
* When you’re designing a framework or library that others will extend.

---