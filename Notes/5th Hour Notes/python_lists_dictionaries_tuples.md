# Python Lists, Dictionaries & Tuples

This guide covers core Python data structures: **Lists** (slice assignment, mutation methods, and list comprehensions), **Dictionaries** (key-value manipulation, iteration, nested structures, and comprehensions), and **Tuples** (immutability, concatenation, and unpacking).

## Table of Contents

1. [Python Lists](#1-python-lists)
   - [Slice Assignment & Deletion](#slice-assignment--deletion)
   - [Looping & Membership Testing](#looping--membership-testing)
   - [Common List Methods (`append`, `insert`, `pop`, `remove`, `copy`)](#common-list-methods-append-insert-pop-remove-copy)
   - [The `range()` Function & List Comprehensions](#the-range-function--list-comprehensions)
2. [Python Dictionaries](#2-python-dictionaries)
   - [Creating, Accessing & Updating Dictionaries](#creating-accessing--updating-dictionaries)
   - [Iterating Through Dictionaries](#iterating-through-dictionaries)
   - [Dictionary Methods (`pop`, `popitem`, `del`, `copy`, `clear`)](#dictionary-methods-pop-popitem-del-copy-clear)
   - [Nested Dictionaries](#nested-dictionaries)
   - [Dictionary Comprehensions & `dict.fromkeys()`](#dictionary-comprehensions--dictfromkeys)
3. [Python Tuples](#3-python-tuples)
   - [Accessing, Slicing & Concatenating Tuples](#accessing-slicing--concatenating-tuples)
   - [Tuple Methods & Unpacking](#tuple-methods--unpacking)

---

## 1. Python Lists

### Slice Assignment & Deletion

You can replace, insert, or delete elements in a list using slice notation.

> **Important Note:** When assigning a string to a slice, always wrap it in a list (`["Lemon"]`). If you assign a plain string (`"Lemon"`), Python will treat the string as an iterable and insert each letter individually (`'L', 'e', 'm', 'o', 'n'`).

```python
tea_varieties = ['Black', 'Green', 'Oolong', 'White']

# Replace a single element using slicing
tea_varieties[1:2] = ["Lemon"]
print(tea_varieties)             # Output: ['Black', 'Lemon', 'Oolong', 'White']

# Replace multiple elements at once
tea_varieties[1:3] = ["Green", "Masala"]
print(tea_varieties)             # Output: ['Black', 'Green', 'Masala', 'White']
```

#### Inserting & Deleting via Empty Slices
```python
tea_varieties = ['Black', 'Green', 'Masala', 'White']

# Insert elements at index 1 without replacing existing ones
print(tea_varieties[1:1])        # Output: []
tea_varieties[1:1] = ["test", "test"]
print(tea_varieties)             # Output: ['Black', 'test', 'test', 'Green', 'Masala', 'White']

# Delete elements by assigning an empty list [] to the slice
tea_varieties[1:3] = []
print(tea_varieties)             # Output: ['Black', 'Green', 'Masala', 'White']
```

### Looping & Membership Testing

By default, `print()` ends with a newline character (`\n`). You can customize this behavior using the `end` parameter.

```python
tea_varieties = ['Black', 'Green', 'Masala', 'White']

# Print all items on the same line separated by '-'
for tea in tea_varieties:
    print(tea, end="-")
# Output: Black-Green-Masala-White-

# Check if an item exists in the list using 'in'
if "Oolong" in tea_varieties:
    print("I have Oolong tea")
```

### Common List Methods (`append`, `insert`, `pop`, `remove`, `copy`)

* **`.append(item)`:** Adds an item to the **end** of the list.
* **`.insert(index, item)`:** Inserts an item at a **specific index**.
* **`.pop()`:** Removes and returns the **last** item from the list.
* **`.remove(item)`:** Removes the first occurrence of a **specific element** by value.
* **`.copy()`:** Creates a shallow copy with a **new memory reference** so changes to the copy do not affect the original list.

```python
tea_varieties = ['Black', 'Green', 'Masala', 'White']

# Append to the end
tea_varieties.append("Oolong")
print(tea_varieties)             # Output: ['Black', 'Green', 'Masala', 'White', 'Oolong']

# Remove the last item
removed_tea = tea_varieties.pop()
print(removed_tea)               # Output: 'Oolong'
print(tea_varieties)             # Output: ['Black', 'Green', 'Masala', 'White']

# Remove a specific item by value
tea_varieties.remove("Green")
print(tea_varieties)             # Output: ['Black', 'Masala', 'White']

# Insert at index 1
tea_varieties.insert(1, "Green")
print(tea_varieties)             # Output: ['Black', 'Green', 'Masala', 'White']

# Independent copy
tea_varieties_copy = tea_varieties.copy()
tea_varieties_copy.append("Lemon")

print(tea_varieties)             # Output: ['Black', 'Green', 'Masala', 'White'] (Unchanged)
print(tea_varieties_copy)        # Output: ['Black', 'Green', 'Masala', 'White', 'Lemon']
```

### The `range()` Function & List Comprehensions

`range(n)` generates numbers from $0$ up to $n - 1$. **List comprehensions** provide a concise way to create lists in a single line.

```python
print(range(10))                 # Output: range(0, 10)

# Squares of numbers from 0 to 9
squared_num = [x**2 for x in range(10)]
print(squared_num)               # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Cubes of numbers from 0 to 4
cube_num = [y**3 for y in range(5)]
print(cube_num)                  # Output: [0, 1, 8, 27, 64]
```

---

## 2. Python Dictionaries

A **Dictionary** stores data in `key: value` pairs. Keys must be unique and immutable.

### Creating, Accessing & Updating Dictionaries

```python
chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}

# Access values using keys
print(chai_types["Masala"])      # Output: 'Spicy'
print(chai_types["Ginger"])      # Output: 'Zesty'

# Update an existing key's value
chai_types["Green"] = "Fresh"
print(chai_types)                # Output: {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}

# Add a new key-value pair
chai_types["Earl Grey"] = "Citrus"
print(chai_types)                # Output: {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
```

### Iterating Through Dictionaries

Each `key: value` pair counts as **one element** when checking `len()`.

```python
chai_types = {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}

# Loop through keys only
for chai in chai_types:
    print(chai)
# Output:
# Masala
# Ginger
# Green

# Loop through keys and access values
for chai in chai_types:
    print(chai, chai_types[chai])

# Recommended: Loop through both keys and values using .items()
for key, value in chai_types.items():
    print(key, value)
# Output:
# Masala Spicy
# Ginger Zesty
# Green Fresh

# Check if a key exists
if "Masala" in chai_types:
    print("I have Masala chai")

# Check total number of key-value pairs
print(len(chai_types))           # Output: 3
```

### Dictionary Methods (`pop`, `popitem`, `del`, `copy`, `clear`)

```python
chai_types = {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}

# .pop(key): Removes the specified key and returns its value
chai_types.pop("Ginger")         # Output: 'Zesty'
print(chai_types)                # Output: {'Masala': 'Spicy', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}

# .popitem(): Removes and returns the last inserted key-value pair as a tuple
chai_types.popitem()             # Output: ('Earl Grey', 'Citrus')
print(chai_types)                # Output: {'Masala': 'Spicy', 'Green': 'Fresh'}

# del: Deletes a specific key-value pair
del chai_types["Green"]
print(chai_types)                # Output: {'Masala': 'Spicy'}

# .copy(): Creates a separate copy of the dictionary
chai_types_copy = chai_types.copy()
chai_types_copy["Chai"] = "Elaichi"

print(chai_types)                # Output: {'Masala': 'Spicy'} (Unchanged)
print(chai_types_copy)           # Output: {'Masala': 'Spicy', 'Chai': 'Elaichi'}
```

### Nested Dictionaries

Dictionaries can contain other dictionaries as values, allowing you to structure hierarchical data.

```python
tea_shop = {
    "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
    "Tea": {"Green": "Mild", "Black": "Strong"}
}

# Accessing nested dictionary values
print(tea_shop["chai"])              # Output: {'Masala': 'Spicy', 'Ginger': 'Zesty'}
print(tea_shop["chai"]["Ginger"])    # Output: 'Zesty'
```

### Dictionary Comprehensions & `dict.fromkeys()`

* **Dictionary Comprehension:** Creates dictionaries dynamically using `{key: value for item in iterable}`.
* **`dict.fromkeys(keys, default_value)`:** Creates a new dictionary from a sequence of keys, assigning the same default value to each key.

```python
# Dictionary Comprehension: Number mapped to its square
squared_num = {x: x**2 for x in range(6)}
print(squared_num)               # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Empty the dictionary
squared_num.clear()
print(squared_num)               # Output: {}

# Creating a dictionary from a list of keys
keys = ["Masala", "Ginger", "Lemon"]
default_value = "Yum"

new_dict = dict.fromkeys(keys, default_value)
print(new_dict)                  # Output: {'Masala': 'Yum', 'Ginger': 'Yum', 'Lemon': 'Yum'}

# Passing a list as the default value assigns that list to every key
new_dict_list = dict.fromkeys(keys, keys)
print(new_dict_list)
# Output: {'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}
```

---

## 3. Python Tuples

A **Tuple** is an ordered, **immutable** collection of items enclosed in parentheses `()`. Once created, elements in a tuple cannot be modified, added, or removed.

### Accessing, Slicing & Concatenating Tuples

```python
tea_types = ("Black", "Green", "Oolong")

# Indexing & Slicing
print(tea_types[0])              # Output: 'Black'
print(tea_types[-1])             # Output: 'Oolong'
print(tea_types[1:])             # Output: ('Green', 'Oolong')
print(len(tea_types))            # Output: 3

# Concatenating tuples using '+' creates a new tuple
more_tea = ("Herbal", "Earl Grey")
all_tea = more_tea + tea_types
print(all_tea)                   # Output: ('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')

# Membership check
if "Green" in all_tea:
    print("I have green tea")
```

### Tuple Methods & Unpacking

* **`.count(value)`:** Returns the number of times a specified value appears in the tuple.
* **Unpacking:** Allows you to assign tuple elements directly into individual variables in a single line.

```python
# Counting occurrences
more_tea = ("Herbal", "Earl Grey", "Herbal")
print(more_tea.count("Herbal"))  # Output: 2
print(more_tea.count("Herb"))    # Output: 0

# Tuple Unpacking
tea_types = ("Black", "Green", "Oolong")
(black, green, oolong) = tea_types

print(black)                     # Output: 'Black'
print(green)                     # Output: 'Green'
print(type(tea_types))           # Output: <class 'tuple'>
```