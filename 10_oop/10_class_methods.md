# Class Methods and Static Methods

* In Python, **class methods** are methods that are bound to the **class** rather than the **instance** of the class.

* They are defined using the `@classmethod` decorator, and by convention, their first parameter is named `cls` (representing the class itself).

---

### Key Points:

- **Instance methods** (default) → take `self` (object) as the first argument.
- **Class methods** → take `cls` (class) as the first argument.
- **Static methods** → take neither `self` nor `cls`.

---

### Syntax:

```python
class MyClass:
    @classmethod
    def my_class_method(cls, arg1, arg2):
        # cls refers to the class
        print(f"Called with: {arg1}, {arg2}")
        print(f"cls is: {cls}")
```

---

### Example 1: Basic Usage

```python
class Student:
    school_name = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

# Access class method using class
Student.change_school("XYZ School")

# Create instance
s1 = Student("Arun")
print(s1.school_name)   # XYZ School
```

🔹 Here `change_school` modifies the **class attribute** for all instances.

---

### Example 2: Alternative Constructor

Class methods are often used as **factory methods** to create objects in different ways.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data_str):
        name, age = data_str.split("-")
        return cls(name, int(age))

# Create object using normal constructor
p1 = Person("Alice", 25)

# Create object using class method
p2 = Person.from_string("Bob-30")

print(p2.name, p2.age)   # Bob 30
```

---

✅ **When to use class methods?**

1. When you want a method that affects the **class as a whole** (not just one object).
2. When creating **alternative constructors** (factory methods).

---

Do you want me to also compare **class methods vs static methods** with examples, so you can clearly see the difference?
