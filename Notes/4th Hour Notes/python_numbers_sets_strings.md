# Python Numbers, Sets & Strings

This guide covers essential Python built-in modules and data types, including the `random` module, high-precision arithmetic with `Decimal` and `Fraction`, `Set` operations, and comprehensive `String` manipulation methods.

## Table of Contents

1. [The `random` Module](#1-the-random-module)
2. [Floating-Point Precision: `Decimal` & `Fraction`](#2-floating-point-precision-decimal--fraction)
3. [Python Sets & Set Operations](#3-python-sets--set-operations)
4. [Strings: Indexing, Slicing & Immutability](#4-strings-indexing-slicing--immutability)
5. [Common String Methods & Formatting](#5-common-string-methods--formatting)

---

## 1. The `random` Module

Python's built-in `random` module is used to generate pseudo-random numbers and perform random operations on sequences.

### Generating Random Integers
`random.randint(a, b)` returns a random integer $N$ such that $a \le N \le b$ (both endpoints are included). *(Note: Unlike `randint()`, functions like `random.randrange(a, b)` exclude the upper limit).*

```python
import random

print(random.randint(1, 10))  # Output: e.g., 8
print(random.randint(1, 10))  # Output: e.g., 6
print(random.randint(1, 10))  # Output: e.g., 7
```

### Working with Lists (`choice` and `shuffle`)
* **`random.choice(seq)`:** Picks a single random element from a non-empty list or sequence.
* **`random.shuffle(seq)`:** Randomly reorders the elements of a list **in place** (modifies the original list).

```python
import random

chai_flavors = ['lemon', 'masala', 'ginger', 'mint']

# Pick a random item
print(random.choice(chai_flavors))  # Output: 'lemon'
print(random.choice(chai_flavors))  # Output: 'ginger'

# Shuffle the list in place
random.shuffle(chai_flavors)
print(chai_flavors)                 # Output: ['mint', 'masala', 'ginger', 'lemon']
```

---

## 2. Floating-Point Precision: `Decimal` & `Fraction`

### Floating-Point Arithmetic Issue
Standard floating-point numbers in Python (and most programming languages) can produce slight precision inaccuracies due to how binary hardware represents decimals.

```python
print(0.1 + 0.1 + 0.1)          # Output: 0.30000000000000004
print((0.1 + 0.1 + 0.1) - 0.3)  # Output: 5.551115123125783e-17
```

### Using `Decimal` for Exact Precision
To get exact decimal arithmetic (crucial for financial or scientific calculations), import `Decimal` from the `decimal` module and pass numbers as **strings**.

```python
from decimal import Decimal

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1'))                  # Output: Decimal('0.3')
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')) # Output: Decimal('0.0')
```

### Working with `Fraction`
The `fractions` module allows you to work directly with rational numbers (numerator over denominator).

```python
from fractions import Fraction

my_fraction = Fraction(2, 7)    # Represents 2/7
print(my_fraction)              # Output: 2/7
print(repr(my_fraction))        # Output: Fraction(2, 7)
```

---

## 3. Python Sets & Set Operations

A **Set** is an unordered collection of unique elements. Sets support mathematical operations like intersection, union, and difference.

```python
set_one = {1, 2, 3, 4}

# Intersection (&): Returns elements common to both sets
print(set_one & {1, 3})         # Output: {1, 3}

# Union (|): Combines all unique elements from both sets
print(set_one | {1, 3})         # Output: {1, 2, 3, 4}
print(set_one | {1, 3, 7})      # Output: {1, 2, 3, 4, 7}

# Difference (-): Removes elements of the second set from the first
print(set_one - {1, 2, 3, 4})   # Output: set()
```

> **Important Note on Empty Sets:**  
> An empty set is always represented as `set()`, **not** `{}`. Using empty curly braces `{}` creates an empty **dictionary** (`<class 'dict'>`).
> ```python
> print(type({}))     # Output: <class 'dict'>
> print(type(set()))  # Output: <class 'set'>
> ```

---

## 4. Strings: Indexing, Slicing & Immutability

### Indexing & Basic Slicing
Strings are ordered sequences of characters. You can access individual characters using zero-based indexing or extract substrings using slicing (`string[start:end]`, where `end` is exclusive).

```python
name = "Anas"
first_char = name[0]
print(first_char)               # Output: A

full_name = "Muhd Anas"
slice_name = full_name[0:4]     # Extracts characters from index 0 up to 3
print(slice_name)               # Output: Muhd
```

### Slicing with Step (`[start:end:step]`)
The third parameter in slicing specifies the **step** (how many characters to skip). A step of `2` picks every second character (skipping 1 character in between).

```python
num_list = "0123456789"

print(num_list[:])              # Output: '0123456789' (Full copy)
print(num_list[3:])             # Output: '3456789'    (From index 3 to the end)
print(num_list[:7])             # Output: '0123456'    (From start up to index 6)
print(num_list[0:7:2])          # Output: '0246'       (Step of 2: skips 1 char)
print(num_list[0:7:3])          # Output: '036'        (Step of 3: skips 2 chars)
```

### String Immutability
Strings in Python are **immutable**—meaning once created, they cannot be changed in place. Methods like `.lower()` or `.upper()` return a **new** string without altering the original variable.

```python
name = "Muhd Anas"

print(name.lower())             # Output: muhd anas
print(name.upper())             # Output: MUHD ANAS
print(name)                     # Output: 'Muhd Anas' (Original remains unchanged)
```

---

## 5. Common String Methods & Formatting

### Cleaning & Replacing Text
* **`.strip()`:** Removes leading and trailing whitespace (extremely useful in web development and form handling).
* **`.replace(old, new)`:** Replaces occurrences of a substring with another string.

```python
raw_name = "   Muhd Anas  "
print(raw_name.strip())                         # Output: 'Muhd Anas'

clean_name = "Muhd Anas"
print(clean_name.replace("Muhd", "Muhammad"))   # Output: 'Muhammad Anas'
print(clean_name)                               # Output: 'Muhd Anas' (Original unchanged)
```

### Searching Substrings with `.find()`
`.find()` returns the starting index of the first occurrence of a substring. If the substring is not found, it returns `-1` (case-sensitive).

```python
car_brand = "Toyota Car"

print(car_brand.find("Car"))    # Output: 7
print(car_brand.find("car"))    # Output: -1 (Not found due to case sensitivity)
```

### Converting Between Strings and Lists (`.split()` & `.join()`)
* **`.split(separator)`:** Splits a string into a list based on a delimiter.
* **`separator.join(list)`:** Joins elements of a list into a single string using the specified separator.

```python
# String to List
cars = "Merce, Audi, BMW"
print(cars.split(", "))                 # Output: ['Merce', 'Audi', 'BMW']

# List to String
chai_variety = ["Lemon", "Masala", "Ginger"]
print("".join(chai_variety))            # Output: LemonMasalaGinger
print(" ".join(chai_variety))           # Output: Lemon Masala Ginger
print("-".join(chai_variety))           # Output: Lemon-Masala-Ginger
print(", ".join(chai_variety))          # Output: Lemon, Masala, Ginger
```

### String Formatting with Placeholders (`.format()`)
Curly braces `{}` act as placeholders inside a string, which can be dynamically populated using `.format()`.

```python
chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"

print(order.format(quantity, chai_type))  # Output: I ordered 2 cups of Masala chai
```