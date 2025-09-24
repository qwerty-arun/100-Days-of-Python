# Inheritance and Composition
- In **Python (and object-oriented programming in general)**, **composition** is a way to build complex objects by combining (or “composing”) other objects, rather than using inheritance.

### 👉 Put simply:

* **Inheritance**: *“is-a”* relationship (e.g., a `Car` **is a** `Vehicle`).
* **Composition**: *“has-a”* relationship (e.g., a `Car` **has an** `Engine`).

---

### Example of Composition

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "Engine started"


class Car:
    def __init__(self, brand, horsepower):
        self.brand = brand
        # Car has an Engine (composition)
        self.engine = Engine(horsepower)

    def start(self):
        return f"{self.brand} car -> {self.engine.start()}"


# Usage
my_car = Car("Tesla", 500)
print(my_car.start())         # Tesla car -> Engine started
print(my_car.engine.horsepower)  # 500
```

Here:

* `Car` **has** an `Engine`.
* Instead of inheriting from `Engine`, we create an `Engine` object inside `Car`.

---

### Why use Composition?

✅ More flexible than inheritance (you can change components without affecting other parts).
✅ Encourages modular design (each class does one thing well).
✅ Avoids deep inheritance chains that become hard to manage.

---

### ⚖️ Rule of thumb:

* Use **inheritance** when there’s a clear “is-a” relationship.
* Use **composition** when there’s a “has-a” relationship.

---

# Comparing Inheritance and Composition

---

## 🚗 Example Scenario: A Car with an Engine

### 1. Using **Inheritance**

```python
# Engine is the parent
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "Engine started"


# Car inherits from Engine (IS-A relationship)
class Car(Engine):
    def __init__(self, brand, horsepower):
        super().__init__(horsepower)
        self.brand = brand

    def start(self):
        return f"{self.brand} car -> {super().start()}"


# Usage
car1 = Car("Tesla", 500)
print(car1.start())          # Tesla car -> Engine started
print(car1.horsepower)       # 500
```

Here:

* `Car` **is-a** `Engine`, which doesn’t make sense in the real world.
* If later you want `Car` to have *two* engines, or a battery, inheritance becomes limiting.

---

### 2. Using **Composition**

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "Engine started"


# Car has an Engine (HAS-A relationship)
class Car:
    def __init__(self, brand, horsepower):
        self.brand = brand
        self.engine = Engine(horsepower)

    def start(self):
        return f"{self.brand} car -> {self.engine.start()}"


# Usage
car2 = Car("Tesla", 500)
print(car2.start())             # Tesla car -> Engine started
print(car2.engine.horsepower)   # 500
```

Here:

* `Car` **has** an `Engine` → matches the real-world relationship.
* You can later replace `Engine` with `ElectricMotor` without touching the rest of the `Car` class.

---

### ✅ Key Takeaway

* **Inheritance** → Use when one class is a specialized version of another (*is-a*).
* **Composition** → Use when one class contains another (*has-a*).

---

Would you like me to also show you a **real-world Python project example** (like a game or banking system) where composition is more powerful than inheritance?
