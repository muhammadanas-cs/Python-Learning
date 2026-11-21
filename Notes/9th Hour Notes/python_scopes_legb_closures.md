# Python Scopes (LEGB) & Closures

This guide covers how Python resolves variable names using the **LEGB Scope Rule**, how to modify global variables inside functions with the `global` keyword, and how **Closures** retain access to enclosing scope variables even after outer functions finish executing.

## Table of Contents

1. [What is Scope? (The LEGB Rule)](#1-what-is-scope-the-legb-rule)
2. [Local vs. Global Scope](#2-local-vs-global-scope)
3. [Modifying Global Variables (`global` Keyword)](#3-modifying-global-variables-global-keyword)
4. [Enclosing Scope & Returning Functions](#4-enclosing-scope--returning-functions)
5. [Python Closures](#5-python-closures)
6. [Scope vs. Closure: Key Differences](#6-scope-vs-closure-key-differences)

---

## 1. What is Scope? (The LEGB Rule)

**Scope** refers to the region of a program where a variable is recognized and can be accessed. Python searches for variables in four hierarchical levels, known as the **LEGB Rule**:

1. **L — Local:** Variables defined inside the current function.
2. **E — Enclosing:** Variables defined in an outer (enclosing) function that contains a nested inner function.
3. **G — Global:** Variables defined at the top level of a module or script.
4. **B — Built-in:** Pre-defined names provided by Python itself (e.g., `print()`, `len()`, `range()`).

---

## 2. Local vs. Global Scope

Variables created inside a function belong to the **local scope** of that function and do not overwrite variables with the same name in the **global scope**.

### Example 1: Local Variable Shadowing Global Variable

```python
x = 10  # Global scope

def greet():
    x = 5  # Local scope (creates a separate local variable)
    print(x)

greet()    # Output: 5
print(x)   # Output: 10 (Global variable remains unchanged)
```

### Example 2: Accessing Global Variables Inside a Function

If a variable is not found in the local scope, Python looks up to the global scope to read its value.

```python
username = "pythonlearning"  # Global scope

def func():
    username = "python"      # Local scope
    print(username)

print(username)              # Output: pythonlearning
func()                       # Output: python
```

```python
x = 99  # Global scope

def func2(y):
    z = x + y                # Reads 'x' from the global scope (99)
    return z

result = func2(1)
print(result)                # Output: 100
```

---

## 3. Modifying Global Variables (`global` Keyword)

By default, assigning a value to a variable inside a function creates a new local variable. To explicitly modify a global variable from inside a function, use the **`global`** keyword.

```python
x = 99  # Global scope

def func3():
    global x  # Points directly to the global variable 'x'
    x = 12    # Modifies the global 'x'

func3()
print(x)      # Output: 12
```

> **Best Practice:** Avoid overusing the `global` keyword in large projects, as modifying global state from inside functions can make debugging harder.

---

## 4. Enclosing Scope & Returning Functions

In Python, functions are first-class objects—meaning you can define a function inside another function and return the inner function as a value.

```python
def f1():
    x = 88          # Enclosing scope variable
    def f2():
        print(x)    # Accesses 'x' from the enclosing scope
    return f2       # Returns the function reference (without executing it)

my_result = f1()    # 'my_result' now holds the reference to 'f2'
my_result()         # Adding '()' executes 'f2' -> Output: 88
```

> **Note:** In Python, referencing a function name (`return f2`) passes the function object itself, while adding parentheses (`my_result()`) executes it.

---

## 5. Python Closures

A **Closure** is an inner function that **remembers and retains access** to variables from its enclosing scope, even after the outer function has finished executing and been removed from the call stack.

```python
def aicoder(num):           # Outer function (Enclosing scope)
    def actual(x):          # Inner function
        return x ** num     # Uses 'num' from enclosing scope
    return actual           # Returns the inner function reference

# Creating two independent closures with different enclosing values
f = aicoder(2)              # Remembers num = 2
g = aicoder(3)              # Remembers num = 3

print(f)                    # Output: <function aicoder.<locals>.actual at 0x...>
print(g)                    # Output: <function aicoder.<locals>.actual at 0x...>

# Executing the closures by passing 'x'
print(f(3))                 # Calculates 3 ** 2 -> Output: 9
print(g(3))                 # Calculates 3 ** 3 -> Output: 27
```

### How It Works Step-by-Step:
1. `aicoder(num)` is the outer function, and `actual(x)` is the inner function.
2. `f = aicoder(2)` executes `aicoder` with `num = 2` and returns `actual` without calling it—creating a closure where `num` is locked in as `2`.
3. `g = aicoder(3)` creates a second, separate closure where `num` is locked in as `3`.
4. Calling `f(3)` passes `x = 3` into `actual(x)`, computing $3^2 = 9$.
5. Calling `g(3)` passes `x = 3` into `actual(x)`, computing $3^3 = 27$.

> **Important:** You cannot call `actual(2)` directly from outside `aicoder()`, because `actual` only exists within `aicoder`'s local scope.

---

## 6. Scope vs. Closure: Key Differences

| Concept | Definition | Primary Role |
| :--- | :--- | :--- |
| **Scope** | The rules (LEGB) determining where variables are visible and accessible in code. | Controls variable visibility and lifetime during execution. |
| **Closure** | A function object bundled together with references to its enclosing scope variables. | Allows an inner function to remember enclosing state after the outer function ends. |