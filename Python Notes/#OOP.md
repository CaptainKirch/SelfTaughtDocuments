### **### Object-Oriented Programming (OOP) in Python**

### **Introduction to OOP**

- Object-Oriented Programming (OOP) allows programmers to create their own objects that have methods and attributes.
- OOP is useful for **scaling code** and **reusing functionality**.
- When working on a large codebase, functions alone are not enough. OOP provides a way to create **custom objects** and **repeatable tasks** in a scalable manner.
- **Basic Class Syntax**:
    
    ```python
    class NameOfClass():
        def __init__(self, param1, param2):
            self.param1 = param1
            self.param2 = param2
    
        def some_method(self):
            # Perform some action
            print(self.param1)
    
    ```
    

### **Understanding the Key Components of OOP**

1. **The `class` Keyword**
    - Used to define an object template.
    - Python uses `CamelCase` naming convention for class names (e.g., `MyClass`).
2. **The `__init__()` Method (Constructor)**
    - A special method called when an object is instantiated.
    - It initializes attributes (variables specific to the object).
3. **Instance Methods**
    - Defined within a class and operate on an instance of that class.
    - Must include `self` as the first parameter to reference instance attributes.

### **Attributes and Class Keyword**

```python
class Dog():
    def __init__(self, breed):  # "__init__" acts as a constructor.
        # "self" represents the instance of the object itself.
        self.breed = breed

# Creating an instance of the class
my_dog = Dog(breed="Lab")
print(my_dog.breed)  # Output: Lab

```

### **Class Object Attributes and Methods**

```python
class Dog():
    # Class attribute (shared across all instances)
    species = "mammal"

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    # Instance Method
    def bark(self):
        print(f"Woof! My name is {self.name}")

# Creating an instance
my_dog = Dog("Labrador", "Buddy", False)
print(my_dog.species)  # Output: mammal
my_dog.bark()  # Output: Woof! My name is Buddy

```

### **Inheritance and Polymorphism**

**Inheritance** - Enables a new class to reuse attributes and methods from an existing class.

```python
class Animal():  # Base class
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

# Dog class inherits from Animal
class Dog(Animal):
    def __init__(self):
        super().__init__()  # Calls the parent class constructor
        print("Dog Created")

    def bark(self):
        print("Woof!")

# Creating an instance
my_dog = Dog()  # Output: Animal Created \n Dog Created
my_dog.who_am_i()  # Output: I am an animal
my_dog.bark()  # Output: Woof!

```

**Polymorphism** - Different classes can share the same method name.

```python
class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Woof!"

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Meow!"

niko = Dog("Niko")
felix = Cat("Felix")

for pet in [niko, felix]:
    print(pet.speak())

# Output:
# Niko says Woof!
# Felix says Meow!

```

### **Special (Magic/Dunder) Methods**

**Dunder (Double Underscore) Methods** are special methods that Python calls automatically when specific operations are performed.

```python
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

my_book = Book("Python Crash Course", "Eric Matthes", 550)
print(my_book)  # Output: Python Crash Course by Eric Matthes
print(len(my_book))  # Output: 550

```

---