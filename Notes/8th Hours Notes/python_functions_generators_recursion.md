# Python Functions, Generators & Recursion

This guide covers the core concepts of **Python Functions**—including parameters vs. arguments, positional and keyword arguments, default values, `lambda` expressions, variable-length arguments (`*args` and `**kwargs`), generator functions using `yield`, and recursion.

## Table of Contents

1. [Parameters vs. Arguments](#1-parameters-vs-arguments)
2. [Types of Function Arguments](#2-types-of-function-arguments)
   * [Default Parameter Values](#default-parameter-values)
   * [Positional Arguments](#positional-arguments)
   * [Keyword Arguments](#keyword-arguments)
3. [Lambda Functions](#3-lambda-functions)
4. [Variable-Length Arguments (`*args` & `**kwargs`)](#4-variable-length-arguments-args--kwargs)
5. [Generators & `yield` vs. `return`](#5-generators--yield-vs-return)
6. [Recursive Functions](#6-recursive-functions)

---

## 1. Parameters vs. Arguments

* **Parameter:** A variable listed inside the parentheses in a function's definition that receives a value when the function is called.
* **Argument:** The actual value passed into the function when calling it.

```python
# 'name' is a parameter
def welcome(name):
    print(f"Welcome, {name}!")

# "Anas" is an argument
welcome("Anas")  # Output: Welcome, Anas!
```

---

## 2. Types of Function Arguments

### Default Parameter Values

A default parameter value is used automatically when no argument is provided for that parameter during the function call.

```python
def greet_user(name="Guest"):
    print(f"Hello, {name}!")

greet_user("Anas")   # Output: Hello, Anas!
greet_user()         # Output: Hello, Guest! (Uses default value)
```

### Positional Arguments

A positional argument is assigned to a function parameter strictly based on its **position (order)** in the function call.

```python
def greet(name, power):
    print(name, power)

greet("Gun", "Anas")
# Output: Gun Anas
```

### Keyword Arguments

A keyword argument is passed to a function by explicitly specifying the **parameter's name**, so the order of arguments does not matter.

```python
def greet(name, power):
    print(name, power)

greet(name="Anas", power="Gun")
# Output: Anas Gun
```

---

## 3. Lambda Functions

A **lambda** is a small, anonymous (unnamed) function that can take any number of arguments but can only contain a **single expression**.

```python
# 1. Normal function
def square(x):
    return x * x

print(square(5))          # Output: 25

# 2. Equivalent Lambda function
square_lambda = lambda x: x * x

print(square_lambda(5))   # Output: 25
```

---

## 4. Variable-Length Arguments (`*args` & `**kwargs`)

### `*args` — Variable Positional Arguments

`*args` allows a function to accept **any number of positional arguments**, which Python collects into a **tuple**.

```python
def sum_all(*args):
    print(args)           # Collected as a tuple
    return sum(args)

print(sum_all(1, 2, 3, 4))
# Output:
# (1, 2, 3, 4)
# 10
```

### `**kwargs` — Variable Keyword Arguments

`**kwargs` allows a function to accept **any number of keyword arguments**, which Python collects into a **dictionary**.

```python
def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_profile(name="Anas", language="Python", level="Beginner")
# Output:
# name: Anas
# language: Python
# level: Beginner
```

---

## 5. Generators & `yield` vs. `return`

* **`yield`:** Produces a value, **pauses** the generator function, and preserves its local state so it can continue from where it stopped when the next value is requested.
* **`return`:** Sends back a final value and **completely terminates** the function immediately.

| Feature | `return` | `yield` |
| :--- | :--- | :--- |
| **Execution Flow** | Terminates the function immediately | Pauses execution and saves state |
| **Return Value** | Returns a single value/object | Returns a generator iterator |
| **Multiple Values** | Code after the first `return` is unreachable | Can yield multiple values sequentially |

### 1. `return` Example

```python
def normal_function():
    return 2
    return 4  # Unreachable: The function has already terminated

print(normal_function())
# Output: 2
```

### 2. `yield` Example

```python
def generate_numbers():
    yield 2
    yield 4

for number in generate_numbers():
    print(number)
# Output:
# 2
# 4
```

> **Note:** The generator produces `2` on the first iteration, pauses, and resumes to produce `4` on the next request.

---

## 6. Recursive Functions

A **recursive function** is a function that **calls itself** to break a complex problem down into smaller, identical sub-problems. Every recursive function must have a **base case** to stop calling itself and prevent an infinite loop.

```python
def factorial(n):
    # Base case: stops recursion when n is 0 or 1
    if n == 0 or n == 1:
        return 1
    # Recursive call
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120 (5 * 4 * 3 * 2 * 1)
```