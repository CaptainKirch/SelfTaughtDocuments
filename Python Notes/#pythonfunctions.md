### **Section #6 - Sub Section #1 - `def` Keyword, Syntax, and Basics of Python Functions**

### **Key Takeaways → What are the core concepts?**

- Functions allow for **code reusability** by organizing operations into callable units.
- Functions start with the `def` keyword, followed by a function name in **snake_case** and parentheses with optional parameters.
- Example syntax:

```python
def my_function(number):
    return number * 2

```

- `return` is used instead of `print` within functions to return values.
- Functions can contain other structures like loops or conditionals and can be called multiple times.

---

### **Section #6 - Sub Section #3 - Logic with Python Functions**

### **Key Takeaways → What are the core concepts?**

- Functions **can be combined** to create modular and reusable logic.
- Functions allow for **automation** by stacking multiple function calls in different parts of the code.

---

### **Section #6 - Sub Section #6 - `args` and `*kwargs`**

### **Key Takeaways → What are the core concepts?**

- `args` and `*kwargs` allow functions to accept a **variable number of arguments**.
- `args` collects multiple values into a tuple.
- `*kwargs` collects named arguments into a dictionary.

Example of `*args`:

```python
def myfunc(*args):
    return sum(args) * 0.05

myfunc(40, 60, 200, 220, 340, 200)  # Can accept any number of arguments

```

Example of `**kwargs`:

```python
def myfunc(**kwargs):
    if "fruit" in kwargs:
        print(f"My fruit of choice is {kwargs['fruit']}")
    else:
        print("No fruit found")

myfunc(fruit="apple")

```

- `args` returns a tuple, while `*kwargs` returns a dictionary.

---

### **Section #6 - Sub Section #7 - Lambda Expressions, Map, and Filter Functions**

### **Key Takeaways → What are the core concepts?**

- **Lambda expressions** are **anonymous functions** used for one-time operations.
- `map()` applies a function to all items in an iterable.
- `filter()` filters elements based on a condition.

**Example of `map()`:**

```python
def square(num):
    return num ** 2

my_nums = [1, 2, 3, 4, 5]
list(map(square, my_nums))

```

**Example of `filter()`:**

```python
def check_even(num):
    return num % 2 == 0

mynums = [1, 2, 3, 4, 5, 6]
list(filter(check_even, mynums))

```

**Example of Lambda Expressions:**

```python
square = lambda num: num ** 2
print(square(5))

```

Using `lambda` with `map()`:

```python
list(map(lambda num: num ** 2, mynums))

```

Using `lambda` with `filter()`:

```python
list(filter(lambda num: num % 2 == 0, mynums))

```

---

### **Section #6 - Sub Section #8 - Nested Statements and Scope**

### **Key Takeaways → What are the core concepts?**

- **LEGB Rule** determines variable scope:
    - **L (Local):** Variables assigned inside functions.
    - **E (Enclosing):** Variables assigned in outer functions.
    - **G (Global):** Variables assigned at the top-level of a module.
    - **B (Built-in):** Predefined Python keywords (e.g., `open`, `range`).

---

This document is now organized and optimized for clarity. Let me know if you need any refinements or additional sections! 🚀