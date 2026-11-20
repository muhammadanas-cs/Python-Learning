<!-- Hour 2 -->
# Python Data Types

Python data types describe the kind of value a variable stores. You can check a value's type with `type()`.

```python
age = 21
name = "Anas"
print(type(age))   # <class 'int'>
print(type(name))  # <class 'str'>
```

## 1. Numeric Types

Python has three built-in numeric types:

| Type | Description | Example |
|---|---|---|
| `int` | Whole numbers | `1234`, `-7` |
| `float` | Decimal numbers | `3.14`, `-0.5` |
| `complex` | Numbers with real and imaginary parts | `3 + 4j` |

Other ways to represent or work with numbers:

```python
binary_number = 0b111  # Binary literal: decimal value 7

from decimal import Decimal
price = Decimal("0.1")  # Useful for decimal arithmetic

from fractions import Fraction
ratio = Fraction(1, 3)  # Represents 1/3 exactly
```

## 2. String (`str`)

A string is a sequence of characters. Strings can use single quotes, double quotes, or triple quotes.

```python
single = 'Hello'
double = "World"
multiline = """This is
a multiline string."""

name = "Anas"
message = f"Hello, {name}!"  # Formatted string (f-string)
```

**Important:** Strings are immutable, which means you cannot change an individual character in place.

```python
word = "Python"
print(word[0])  # P
print(word[1:4])  # yth
```

## 3. List (`list`)

A list is an ordered, mutable collection. It can contain different data types and duplicate values.

```python
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
mixed = [1, "hello", True]
nested = [1, 2, 3, ['a', 'b']]
from_range = list(range(5))  # [0, 1, 2, 3, 4]

numbers.append(4)  # Adds an item
numbers[0] = 10    # Updates an item
```

Use square brackets `[]` to create a list.

## 4. Tuple (`tuple`)

A tuple is an ordered, immutable collection. It can contain duplicate values and different data types.

```python
coordinates = (10, 20)
letters = ('a', 'b', 'c')
from_range = tuple(range(5))  # (0, 1, 2, 3, 4)

single_item = (5,)  # Comma is required for a one-item tuple
```

Use parentheses `()` by convention. The comma, rather than the parentheses alone, makes a tuple.

## 5. Dictionary (`dict`)

A dictionary stores data as **key-value pairs**. Keys must be unique and hashable; values can be duplicated.

```python
student = {
    "name": "Anas",
    "marks": 90,
    "passed": True
}

print(student["name"])       # Anas
print(student.get("age"))    # None if the key is missing
student["marks"] = 95        # Update a value
student["age"] = 21          # Add a new key-value pair
```

Use curly braces `{}` with key-value pairs, or `dict()`.

**Important:** Dictionaries are accessed by keys, not by numeric index.

## 6. Set (`set`)

A set is an unordered collection of unique, hashable items. It removes duplicates.

```python
numbers = {1, 2, 2, 3}
print(numbers)  # {1, 2, 3} (display order may vary)

empty_set = set()  # {} creates an empty dictionary, not a set
letters = {'a', 'b', 'c'}

numbers.add(4)
numbers.discard(2)
```

Sets are useful for removing duplicates and performing set operations such as union and intersection.

## 7. Boolean (`bool`)

A Boolean represents one of two values: `True` or `False`.

```python
is_active = True
print(bool(1))   # True
print(bool(0))   # False
print(5 > 2)     # True
```

Values such as `0`, `''`, `[]`, `{}`, `set()`, and `None` are false-like; most other values are true-like.

## 8. None (`NoneType`)

`None` represents the absence of a value.

```python
result = None
print(type(result))  # <class 'NoneType'>

if result is None:
    print("No result yet")
```

Use `is None` to check for `None`.

## 9. Binary data types

Python also has types for working with binary data:

- `bytes`: immutable sequence of bytes, e.g. `b"hello"`
- `bytearray`: mutable sequence of bytes, e.g. `bytearray(b"hello")`
- `memoryview`: provides access to binary data without copying it in some situations

These are useful when working with files, images, and network data.

## 10. Files are handled with file objects

A file path such as `"file.txt"` is a string, not a data type. Calling `open()` returns a file object.

```python
with open("file.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

Common modes:
- `"r"` — read an existing file
- `"w"` — write; creates or overwrites a file
- `"a"` — append to a file
- `"b"` — binary mode, e.g. `"rb"`
- `"+"` — reading and writing, e.g. `"r+"`

Using `with` closes the file automatically when the block finishes.

## 11. Mutable vs. immutable

| Mutable (can be changed) | Immutable (cannot be changed in place) |
|---|---|
| `list` | `int` |
| `dict` | `float` |
| `set` | `bool` |
| `bytearray` | `str` |
| | `tuple` (its contained mutable objects may still change) |
| | `bytes` |
| | `NoneType` |

This distinction matters when updating values and passing objects to functions.

## 12. Checking and converting types

```python
value = 42
print(type(value))       # <class 'int'>
print(isinstance(value, int))  # True

text_number = "123"
number = int(text_number)
decimal_number = float("3.14")
text = str(100)
items = list((1, 2, 3))
```

Conversion only works when the value can be converted; for example, `int("hello")` raises a `ValueError`.

## 13. Collections at a glance

| Type | Ordered? | Mutable? | Allows duplicates? | Access |
|---|---|---|---|---|
| `list` | Yes | Yes | Yes | Index |
| `tuple` | Yes | No (in-place) | Yes | Index |
| `dict` | Insertion order | Yes | Keys: no; values: yes | Key |
| `set` | No guaranteed order | Yes | No | No index |
| `str` | Yes | No | Characters may repeat | Index |

## 14. Other Python concepts (not data types)

These are important Python concepts, but they are **not themselves built-in data types**:

- **Functions** — reusable blocks of code (`def`, `lambda`)
- **Classes** — blueprints used to create objects
- **Modules** — Python files that can be imported
- **Iterators and generators** — ways to produce values one at a time
- **Decorators** — wrap or modify a function or class
- **Context managers** — manage setup and cleanup, often used with `with`
- **Coroutines and `async`/`await`** — support asynchronous programming
- **Metaprogramming** — code that examines or changes program structure

These topics can stay in a separate section of your notes so the data-type list remains accurate.

## Quick revision

- `list`: ordered and mutable
- `tuple`: ordered and immutable
- `dict`: key-value pairs
- `set`: unique items
- `str`: text and immutable
- `bool`: `True` or `False`
- `None`: absence of a value
- `type(x)`: checks the type of `x`
- `isinstance(x, T)`: checks whether `x` is an instance of type `T`
