# Python Decorators & Practical Examples

This guide covers **Python Decorators**—how they work under the hood, the core concepts required to build them, and step-by-step breakdowns of three classic decorator problems: **Execution Timing**, **Call Debugging**, and **Caching (Memoization)**.

## Table of Contents

1. [What is a Decorator?](#1-what-is-a-decorator)
2. [Core Concepts Used in Decorators](#2-core-concepts-used-in-decorators)
3. [Problem 1: Timing Function Execution (`@timer`)](#3-problem-1-timing-function-execution-timer)
4. [Problem 2: Debugging Function Calls (`@debug`)](#4-problem-2-debugging-function-calls-debug)
5. [Problem 3: Caching Return Values (`@cache`)](#5-problem-3-caching-return-values-cache)

---

## 1. What is a Decorator?

A **Decorator** is a design pattern in Python that allows you to **add new functionality to an existing function** without modifying its original source code.

Decorators work because functions in Python are **first-class objects**—they can be passed as arguments to other functions, defined inside another function, and returned as values.

### How the `@` Syntax Works
Using `@decorator_name` above a function is simply syntactic sugar:

```python
@timer
def example_function(n):
    pass

# Behind the scenes, Python executes:
# example_function = timer(example_function)
```

---

## 2. Core Concepts Used in Decorators

To understand and write decorators effectively, you need a solid grasp of the following concepts used across the three solutions:

1. **Nested Functions (`wrapper`):** A decorator defines an inner `wrapper()` function that wraps around the original `func()`, runs extra logic before/after calling `func()`, and returns the result.
2. **Closures:** The `wrapper()` function remembers `func` (and any local variables like `cache_value`) from the outer decorator's enclosing scope even after the outer decorator function finishes executing.
3. **`*args` and `**kwargs`:** Used in `wrapper(*args, **kwargs)` so the decorator can accept **any number of positional and keyword arguments** and forward them cleanly to `func(*args, **kwargs)`.
4. **Function Metadata (`func.__name__`):** Every function object in Python has built-in attributes. `func.__name__` retrieves the original function's name as a string (useful for logging and debugging).
5. **The `time` Module (`time.time()` & `time.sleep()`):**
   * `time.time()` returns the current timestamp in seconds (used to calculate elapsed time: `end - start`).
   * `time.sleep(n)` pauses program execution for `n` seconds (used to simulate slow/heavy tasks).
6. **Generator Expressions & `.join()`:** Used in Problem 2 (`', '.join(str(arg) for arg in args)`) to format arguments cleanly into a single comma-separated string.
7. **Memoization (Dictionary Caching):** Storing function results in a dictionary (`cache_value = {}`) using the arguments tuple (`args`) as the key so repeated calls return instantly without re-running expensive logic.

---

## 3. Problem 1: Timing Function Execution (`@timer`)

**Goal:** Measure and print how long a function takes to execute.

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()                # Record start time
        result = func(*args, **kwargs)     # Execute the original function
        end = time.time()                  # Record end time
        print(f"{func.__name__} ran in {end - start} time")
        return result                      # Return the original function's output
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(2)
# Output: example_function ran in 2.000123... time
```

### Key Takeaways
* `result = func(*args, **kwargs)` captures the return value of the wrapped function so it isn't lost when `wrapper` finishes.
* Subtracting `start` from `end` gives the total execution duration in seconds.

---

## 4. Problem 2: Debugging Function Calls (`@debug`)

**Goal:** Print the function's name along with all positional and keyword arguments every time the function is called.

```python
def debug(func):
    def wrapper(*args, **kwargs):
        # Format positional arguments into a comma-separated string
        args_value = ', '.join(str(arg) for arg in args)
        # Format keyword arguments as key=value pairs
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        
        print(f"Calling: {func.__name__} with args ({args_value}) and kwargs ({kwargs_value})")
        return func(*args, **kwargs)
    return wrapper

@debug
def hello():
    print("hello")

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

hello()
# Output:
# Calling: hello with args () and kwargs ()
# hello

greet("coffee", greeting="okay")
# Output:
# Calling: greet with args (coffee) and kwargs (greeting=okay)
# okay, coffee
```

### Key Takeaways
* When `hello()` is called with no arguments, `args` is an empty tuple `()` and `kwargs` is an empty dictionary `{}`, resulting in empty strings for both formatted variables.
* Using `str(arg)` ensures non-string arguments (like integers or lists) can be safely joined without raising a `TypeError`.

---

## 5. Problem 3: Caching Return Values (`@cache`)

**Goal:** Cache return values in memory so that calling the function again with the same arguments returns the saved result immediately without re-executing the function.

```python
import time

def cache(func):
    cache_value = {}  # Persists across calls via closure
    
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]       # Return cached result immediately
        
        result = func(*args)               # Compute result if not cached
        cache_value[args] = result         # Save result in cache dictionary
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)                          # Simulates a slow computation
    return a + b

print(long_running_function(2, 3))         # Takes ~4 seconds -> Output: 5
print(long_running_function(2, 3))         # Instant (from cache) -> Output: 5
```

### Key Takeaways
* **`cache_value = {}`** is initialized once when `@cache` decorates `long_running_function`, not every time the function is called.
* Because **`*args` is a tuple** (which is immutable and hashable), it can be used directly as a key in the `cache_value` dictionary (`cache_value[(2, 3)] = 5`).
* On the second call `long_running_function(2, 3)`, `args in cache_value` evaluates to `True`, skipping the 4-second `time.sleep(4)` delay completely.