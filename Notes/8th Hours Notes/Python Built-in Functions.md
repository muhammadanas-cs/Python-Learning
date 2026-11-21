# Essential Python Built-in Functions

## Table of Contents

1. [Input, Output & Inspection](#1-input-output--inspection)
2. [Type Conversion & Data Structures](#2-type-conversion--data-structures)
3. [Math & Aggregation](#3-math--aggregation)
4. [Sequences, Iteration & Functional Tools](#4-sequences-iteration--functional-tools)
5. [Object-Oriented Programming (OOP) & Attributes](#5-object-oriented-programming-oop--attributes)
6. [File Handling & Debugging](#6-file-handling--debugging)

---

## 1. Input, Output & Inspection

### `print()`
Displays output to the console or screen.
```python
print("Hello, Python!", sep=" ", end="\n")
# Output: Hello, Python!
```

### `input()`
Accepts text input from the user as a string.
```python
name = input("Enter your name: ")
print(f"Welcome, {name}!")
```

### `len()`
Returns the total number of items in an object (string, list, tuple, dictionary, etc.).
```python
fruits = ["Apple", "Banana", "Mango"]
print(len(fruits))  # Output: 3
```

### `type()`
Returns the data type (class) of an object.
```python
x = 3.14
print(type(x))  # Output: <class 'float'>
```

### `isinstance()`
Checks whether an object is an instance of a specific class or data type (preferred over `type()` for type checking).
```python
num = 42
print(isinstance(num, int))         # Output: True
print(isinstance(num, (str, int)))  # Output: True
```

### `id()`
Returns the unique memory identity (address) of an object.
```python
a = [1, 2, 3]
print(id(a))  # Output: e.g., 1402348923412
```

---

## 2. Type Conversion & Data Structures

### `int()`, `float()`, `str()`, `bool()`
Convert values between fundamental data types.
```python
print(int("25") + 5)     # Output: 30
print(float("3.5"))      # Output: 3.5
print(str(100) + "%")    # Output: '100%'
print(bool(0))           # Output: False
print(bool("Python"))    # Output: True
```

### `list()`, `tuple()`, `set()`, `dict()`
Create or convert iterables into Python's core collection data structures.
```python
# list(): Creates a mutable list
print(list("abc"))                     # Output: ['a', 'b', 'c']

# tuple(): Creates an immutable tuple
print(tuple([1, 2, 3]))                # Output: (1, 2, 3)

# set(): Extracts unique items from an iterable
print(set([1, 2, 2, 3, 3]))            # Output: {1, 2, 3}

# dict(): Creates a dictionary from key-value pairs
print(dict([("name", "Anas"), ("age", 22)]))  # Output: {'name': 'Anas', 'age': 22}
```

---

## 3. Math & Aggregation

### `abs()`
Returns the absolute (non-negative) value of a number.
```python
print(abs(-15))   # Output: 15
print(abs(-3.7))  # Output: 3.7
```

### `round()`
Rounds a floating-point number to a specified number of decimal places.
```python
print(round(3.14159, 2))  # Output: 3.14
print(round(4.6))         # Output: 5
```

### `pow()`
Raises a base number to an exponent ($x^y$), with an optional modulus parameter.
```python
print(pow(2, 3))     # Output: 8 (2^3)
print(pow(2, 3, 5))  # Output: 3 ((2^3) % 5)
```

### `min()`, `max()`, `sum()`
Find the smallest item, largest item, or total sum of items in an iterable.
```python
scores = [85, 92, 78, 95]

print(min(scores))  # Output: 78
print(max(scores))  # Output: 95
print(sum(scores))  # Output: 350
```

---

## 4. Sequences, Iteration & Functional Tools

### `range()`
Generates an immutable sequence of integers (commonly used in `for` loops).
```python
for i in range(1, 5):
    print(i, end=" ")
# Output: 1 2 3 4
```

### `sorted()` & `reversed()`
* **`sorted()`:** Returns a **new** sorted list from any iterable without modifying the original.
* **`reversed()`:** Returns a reverse iterator over a sequence.
```python
nums = [4, 1, 3, 2]

print(sorted(nums))                # Output: [1, 2, 3, 4]
print(sorted(nums, reverse=True))  # Output: [4, 3, 2, 1]
print(list(reversed(nums)))        # Output: [2, 3, 1, 4]
```

### `enumerate()`
Adds an automatic counter (index) when looping over an iterable.
```python
languages = ["Python", "JavaScript", "C++"]

for index, lang in enumerate(languages, start=1):
    print(f"{index}. {lang}")
# Output:
# 1. Python
# 2. JavaScript
# 3. C++
```

### `zip()`
Combines elements from multiple iterables into tuples pairwise.
```python
names = ["Anas", "Ahmed", "Sara"]
marks = [90, 85, 95]

combined = list(zip(names, marks))
print(combined)  # Output: [('Anas', 90), ('Ahmed', 85), ('Sara', 95)]
```

### `map()` & `filter()`
* **`map(func, iterable)`:** Applies a function to every item in an iterable.
* **`filter(func, iterable)`:** Keeps only items for which the function returns `True`.
```python
numbers = [1, 2, 3, 4, 5]

# Square every number
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)    # Output: [2, 4]
```

### `any()` & `all()`
* **`any()`:** Returns `True` if **at least one** element in the iterable is truthy.
* **`all()`:** Returns `True` only if **every** element in the iterable is truthy.
```python
conditions = [True, False, True]

print(any(conditions))  # Output: True
print(all(conditions))  # Output: False
```

### `iter()` & `next()`
Manually create an iterator from an iterable and fetch items one by one.
```python
items = iter(["First", "Second"])

print(next(items))  # Output: First
print(next(items))  # Output: Second
```

---

## 5. Object-Oriented Programming (OOP) & Attributes

### `super()`
Calls methods from a parent (base) class inside a child (derived) class.
```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")

c = Child()
c.greet()
# Output:
# Hello from Parent
# Hello from Child
```

### `hasattr()`, `getattr()`, `setattr()`, `delattr()`
Dynamically inspect, read, update, or delete attributes on an object.
```python
class Student:
    name = "Anas"

s = Student()

print(hasattr(s, "name"))       # Output: True
print(getattr(s, "name"))       # Output: Anas

setattr(s, "grade", "A")
print(s.grade)                  # Output: A

delattr(s, "grade")
print(hasattr(s, "grade"))      # Output: False
```

### `staticmethod()` & `classmethod()`
Decorators used to define methods bound to a class rather than an instance.
```python
class MathHelper:
    factor = 10

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply_by_factor(cls, num):
        return num * cls.factor

print(MathHelper.add(3, 4))                 # Output: 7
print(MathHelper.multiply_by_factor(5))     # Output: 50
```

---

## 6. File Handling & Debugging

### `open()`
Opens a file and returns a file object for reading (`"r"`), writing (`"w"`), or appending (`"a"`).
```python
with open("notes.txt", "w") as file:
    file.write("Python built-in functions are awesome!")
```

### `dir()` & `help()`
* **`dir()`:** Lists all valid attributes and methods of an object.
* **`help()`:** Displays built-in documentation for modules, functions, or classes.
```python
print(dir(str))   # Lists all string methods (e.g., 'upper', 'split', 'strip')
help(len)         # Displays official documentation for len()
```

> **Security Note on `eval()` and `exec()`:** Both functions execute strings as Python code dynamically. **Never** pass untrusted user input into `eval()` or `exec()`, as it creates critical security vulnerabilities.