'''markdown

# Object-Oriented Programming (OOP) in Python

Object-Oriented Programming (OOP) is a programming approach that organizes code using **classes and objects**. It helps make code reusable, organized, and easier to maintain.

1. Encapsulation

**Definition:** Encapsulation is the process of wrapping data (attributes) and methods into a single unit (class) and restricting direct access to some data.

- Keeps data protected inside a class.
- Uses private attributes (`__`) to restrict direct access.
- Provides methods or properties to access and modify data.

**Example:**

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

account = BankAccount(5000)

print(account.get_balance())
```

**Output:**
```text
5000
```

Here, `__balance` is a private attribute and is accessed through the `get_balance()` method.

2. Inheritance

**Definition:** Inheritance allows a child class to acquire the attributes and methods of a parent class.

- Promotes code reusability.
- Child classes can use parent class methods.
- Child classes can also add their own methods or override existing ones.

**Example:**

```python
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("Car is starting")


class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")


my_car = ElectricCar("Tesla")

print(my_car.brand)
my_car.start()
my_car.charge()
```

**Output:**
```text
Tesla
Car is starting
Electric car is charging
```

Here, `ElectricCar` inherits the `brand` attribute and `start()` method from the `Car` class.

3. Polymorphism

**Definition:** Polymorphism means "many forms". It allows the same method name to perform different actions depending on the object.

- Different classes can have methods with the same name.
- Each class can provide its own implementation.
- Makes code more flexible.

**Example:**

```python
class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

**Output:**
```text
Dog barks
Cat meows
```

Here, both classes have the same method `sound()`, but each performs a different action.

4. Abstraction

**Definition:** Abstraction means hiding unnecessary implementation details and showing only the essential functionality to the user.

- Hides complex internal implementation.
- Focuses on what an object does rather than how it does it.
- In Python, abstraction can be implemented using the `abc` module and abstract classes.

**Example:**

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Dog barks")


dog = Dog()
dog.sound()
```

**Output:**
```text
Dog barks
```

Here, `Animal` defines an abstract method `sound()`. The `Dog` class provides its actual implementation.

---

Quick Revision

| Concept | Main Purpose |
|---|---|
| Encapsulation | Protecting and controlling access to data |
| Inheritance | Reusing code from parent classes |
| Polymorphism | Same method name, different behaviors |
| Abstraction | Hiding implementation details |

**Remember:**
- Encapsulation = Data Protection
- Inheritance = Code Reusability
- Polymorphism = Many Forms
- Abstraction = Hiding Complexity