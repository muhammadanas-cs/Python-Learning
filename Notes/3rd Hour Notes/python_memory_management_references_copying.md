# Python Memory Management, References & Copying

This guide covers how Python handles memory references, garbage collection, list mutability, slicing, shallow vs. deep copying, equality operators (`==` vs `is`), and string representations (`repr()`, `str()`, and `print()`).

---

## Table of Contents
1. [Reference Counting & Garbage Collection](#1-reference-counting--garbage-collection)
2. [Variable References & List Mutability](#2-variable-references--list-mutability)
3. [List Slicing & Copying](#3-list-slicing--copying)
4. [Difference Between `==` and `is`](#4-difference-between--and-is)
5. [Difference Between `repr()`, `str()`, and `print()`](#5-difference-between-repr-str-and-print)

---

## 1. Reference Counting & Garbage Collection

In Python, everything is an object, and variables act as references (pointers) to these objects in memory. Python tracks how many references point to an object using **reference counting**.

```python
import sys

# Checking reference counts for immutable objects
print(sys.getrefcount(2))        # High count (internally cached by Python)
print(sys.getrefcount(90))       # High count (internally cached by Python)
print(sys.getrefcount("Rafid"))  # Output: 3
print(sys.getrefcount("Hi"))     # Output: 3
```

### Delayed Garbage Collection

Python does **not** immediately delete unreferenced numbers and strings from memory.

```python
a = 2
a = "rafid"
a = 3.14
```

> **Why?** Python knows that numbers and strings are frequently reused in programs. Instead of immediately collecting `2` and `"rafid"` as garbage, Python keeps them in memory briefly so they can be quickly reused if referenced again later.

---

## 2. Variable References & List Mutability

Lists in Python are **mutable** (can be changed in place). Understanding how variables reference lists is crucial to avoid unexpected bugs.

### Example 1: Reassigning a Variable

When you reassign a variable to a new object, the original reference remains intact for any other variable pointing to it.

```python
myListOne = [1, 2, 3]
myListTwo = myListOne    # Both point to the same list in memory

myListOne = "rafid"      # myListOne now points to a new string object
print(myListTwo)         # Output: [1, 2, 3] (Still points to the original list)
```

### Example 2: Reassigning vs. Mutating in Place

Creating a new list with the same values creates a **new object** in memory.

```python
myListOne = [1, 2, 3]
myListTwo = myListOne

myListOne = 'chai'
print(myListTwo)         # Output: [1, 2, 3]

# Assigning a brand new list object with the same values
myListOne = [1, 2, 3]    
# At this point, myListOne and myListTwo point to DIFFERENT list objects in memory.

myListOne[0] = 33        # Modifying myListOne will NOT affect myListTwo
print(myListOne)         # Output: [33, 2, 3]
print(myListTwo)         # Output: [1, 2, 3]
```

### Example 3: Shared References & In-Place Mutation

If two variables point to the **same** list object and you modify an element inside that list, both variables reflect the change.

```python
l1 = [1, 2, 3]
l2 = l1                  # l2 references the exact same list as l1

l1[0] = 44               # Mutating the list in place
print(l1)                # Output: [44, 2, 3]
print(l2)                # Output: [44, 2, 3] (l2 reflects the change)
```

> **Note:** Even if you assign identical values separately, Python creates two distinct list objects in memory:
> ```python
> p1 = [1, 2, 3]
> p2 = [1, 2, 3]  # p1 and p2 are stored at different memory locations
> ```

---

## 3. List Slicing & Copying

Slicing allows you to extract a portion of a list. The syntax is `list[start:end]`, where `start` is inclusive and `end` is **exclusive**.

```python
l1 = [1, 2, 3]
l2 = l1[0:2]             # Includes index 0 and 1 (index 2 is excluded)
print(l2)                # Output: [1, 2]
print(l1)                # Output: [1, 2, 3]
```

### Creating a Shallow Copy via Slicing

Using `[:]` creates a **shallow copy** of the entire list in a new memory location. Modifying the original list will not affect the copied list.

```python
l1 = [1, 2, 3]
l2 = l1[:]               # Creates a new copy of l1

l1[0] = 33
print(l1)                # Output: [33, 2, 3]
print(l2)                # Output: [1, 2, 3] (Unaffected)
```

### `copy.copy()` vs `copy.deepcopy()`

- **`l2 = l1[:]`** and **`copy.copy(l1)`** do the exact same thing (create a shallow copy); slicing is just a shorter syntax.
- **`copy.deepcopy(l1)`** is used when you have nested lists (a list inside a list) and want to copy the inner lists as independent objects as well.

```python
import copy

# Shallow Copy
h1 = [1, 2, [3, 4]]
h2 = copy.copy(h1)       # Outer list is copied, inner list is still shared

# Deep Copy
h3 = copy.deepcopy(h1)   # Both outer and inner lists are completely independent
```

---

## 4. Difference Between `==` and `is`

- **`==` (Equality Operator):** Checks if the **values** of two objects are the same.
- **`is` (Identity Operator):** Checks if both variables point to the **exact same object in memory** (same memory reference).

```python
n = [1, 2, 3]
m = n

print(m == n)            # Output: True (Values are equal)
print(m is n)            # Output: True (Both point to the same memory reference)

# Assigning separate list objects with identical values
n = [1, 2, 3]
m = [1, 2, 3]

print(m == n)            # Output: True (Values are still equal)
print(m is n)            # Output: False (They are two different objects in memory)
```

---

## 5. Difference Between `repr()`, `str()`, and `print()`

Python provides different ways to represent and display objects depending on whether the audience is a developer or an end-user.

| Function | Purpose | Output for `'chai'` |
| :--- | :--- | :--- |
| **`repr()`** | Returns a **developer-oriented** string representation that unambiguously identifies the object (often valid Python syntax). | `"'chai'"` |
| **`str()`** | Converts the object into a clean, **human-readable** string format. | `'chai'` |
| **`print()`** | Outputs the human-readable representation directly to the **console** (returns `None`). | `chai` |

```python
text = 'chai'

print(repr(text))        # Output: 'chai' (Includes quotes showing it's a string)
print(str(text))         # Output: chai
print(text)              # Output: chai
```