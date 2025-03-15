# **Cheat Sheet for Problem Solving**

### **1️⃣ Lists (Arrays)**

### ✅ **Creating a List**

```python
python
CopyEdit
nums = [1, 2, 3, 4]

```

### ✅ **Adding & Removing Elements**

```python
python
CopyEdit
nums.append(5)      # Add at the end → [1, 2, 3, 4, 5]
nums.insert(1, 99)  # Insert at index 1 → [1, 99, 2, 3, 4, 5]
nums.pop()          # Remove last element → [1, 99, 2, 3, 4]
nums.remove(99)     # Remove specific value → [1, 2, 3, 4]

```

### ✅ **List Comprehensions**

```python
python
CopyEdit
squared = [x**2 for x in nums]  # [1, 4, 9, 16]
evens = [x for x in nums if x % 2 == 0]  # Filter evens → [2, 4]

```

### ✅ **Looping Through a List**

```python
python
CopyEdit
for num in nums:
    print(num)  # Prints each number

```

### ✅ **Sorting & Reversing**

```python
python
CopyEdit
nums.sort()        # Sorts in ascending order
nums.sort(reverse=True)  # Sort in descending order
nums.reverse()     # Reverse order of elements

```

---

### **2️⃣ Strings**

### ✅ **String Basics**

```python
python
CopyEdit
s = "hello"
print(s[0])  # h
print(len(s))  # 5

```

### ✅ **String Manipulation**

```python
python
CopyEdit
s.upper()  # HELLO
s.lower()  # hello
s.replace("l", "z")  # hezzo
s.strip()  # Removes whitespace
s.split()  # Converts into list based on spaces

```

### ✅ **String Joining**

```python
python
CopyEdit
words = ["hello", "world"]
sentence = " ".join(words)  # "hello world"

```

---

### **3️⃣ Dictionaries (Hash Maps)**

### ✅ **Creating a Dictionary**

```python
python
CopyEdit
student = {"name": "Alice", "age": 25}

```

### ✅ **Access & Modify**

```python
python
CopyEdit
print(student["name"])  # Alice
student["age"] = 26  # Modify age
student["city"] = "NYC"  # Add new key-value pair

```

### ✅ **Looping Through Dictionary**

```python
python
CopyEdit
for key, value in student.items():
    print(key, value)

```

### ✅ **Checking If a Key Exists**

```python
python
CopyEdit
if "age" in student:
    print("Key exists!")

```

---

### **4️⃣ Sets (Unique Elements)**

### ✅ **Creating a Set**

```python
python
CopyEdit
unique_nums = {1, 2, 3, 4, 4, 5}  # {1, 2, 3, 4, 5}

```

### ✅ **Adding & Removing Elements**

```python
python
CopyEdit
unique_nums.add(10)   # {1, 2, 3, 4, 5, 10}
unique_nums.remove(2)  # {1, 3, 4, 5, 10}

```

### ✅ **Set Operations**

```python
python
CopyEdit
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # Union → {1, 2, 3, 4, 5}
print(a & b)  # Intersection → {3}
print(a - b)  # Difference → {1, 2}

```

---

### **5️⃣ Tuples (Immutable Lists)**

### ✅ **Creating a Tuple**

```python
python
CopyEdit
coords = (3, 4)

```

### ✅ **Accessing Elements**

```python
python
CopyEdit
print(coords[0])  # 3

```

### ✅ **Tuple Unpacking**

```python
python
CopyEdit
x, y = coords

```

---

### **6️⃣ Stacks (LIFO - Last In, First Out)**

- A **stack** is a data structure where the last element added is the first one removed (**LIFO**).
- Use `list.append(x)` to **push** elements and `list.pop()` to **remove** the last added element.

```python
python
CopyEdi
stack = []
stack.append(1)  # Push
stack.append(2)
stack.pop()  # Pop → Removes 2 (last added)

```

---

### **7️⃣ Queues (FIFO - First In, First Out)**

- A **queue** processes elements in the order they were added (**FIFO**).
- Use `collections.deque()` to efficiently remove elements from the front using `.popleft()`.

```python
python
CopyEdit
from collections import deque
queue = deque()
queue.append(1)  # Add to end
queue.append(2)
queue.popleft()  # Removes 1 (first added)

```

---

### **8️⃣ Counter (Counting Occurrences)**

- The `Counter` class from `collections` **counts occurrences** of elements in a list or string.
- Useful for frequency-based problems like finding the most common element.

```python
python
CopyEdit
from collections import Counter
nums = [1, 2, 2, 3, 3, 3]
count = Counter(nums)  # {1:1, 2:2, 3:3}
print(count[2])  # 2 (since 2 appears twice)

```

---

### **9️⃣ Sorting with Custom Key**

- The `sort()` method allows sorting using a **custom key function** (like sorting by length or a specific property).
- Use `sorted()` to return a **new sorted list** without modifying the original.

```python
python
CopyEdit
words = ["banana", "apple", "kiwi"]
words.sort(key=len)  # Sort by length → ['kiwi', 'apple', 'banana']

```

---

### **🔟 Lambda Functions (Anonymous Functions)**

- **Lambda functions** are short, inline functions used when you need a function for a single task.
- Commonly used for **sorting, mapping, and filtering data**.

```python
python
CopyEdit
double = lambda x: x * 2
print(double(5))  # 10

```

---

### **💡 Problem-Solving Templates (Quick Recap)**

### **Find Unique Elements (Using Counter)**

- **Counts occurrences** of elements and **filters only unique ones**.

```python
python
CopyEdit
from collections import Counter
def find_unique(nums):
    count = Counter(nums)
    return [x for x in nums if count[x] == 1]

```

### **Check for Valid Parentheses (Using Stack)**

- **Uses a stack** to track open/close brackets and ensures proper matching.

```python
python
CopyEdit
def is_valid_parentheses(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    return not stack

```

### **Product of Array Except Self (Without Division)**

- **Uses prefix multiplication (left & right)** to compute products **without division**.

```python
python
CopyEdit
def product_except_self(nums):
    n = len(nums)
    output = [1] * n
    left = 1
    for i in range(n):
        output[i] = left
        left *= nums[i]
    right = 1
    for i in range(n-1, -1, -1):
        output[i] *= right
        right *= nums[i]
    return output

```

### **Group Anagrams (Using Dictionary & Sorting)**

- **Sorts each word's letters** and uses a dictionary to **group anagrams** together.

```python

from collections import defaultdict
def group_anagrams(strs):
    anagram_groups = defaultdict(list)
    for word in strs:
        key = tuple(sorted(word))
        anagram_groups[key].append(word)
    return list(anagram_groups.values())

```