# class Car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def display_info(self):
#         return f"My cars make is {self.make}, {self.model}, {self.year}"
    

# my_car = Car(make= "tesla", model= "Y", year=2012)

# print(my_car.display_info())

#---------------------------------------------------------------------
# scores = {"Alice": 85, "Bob": 90, "Charlie": 80}

# sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))

# print(sorted_scores)


#---------------------------------------------------------------------

# colors = ["red","yellow","green"]

# colors.insert(1, "blue")

# print(colors)

#---------------------------------------------------------------------

# nums = [1,2,3,4,2,3,5]

# duplicates = {num for num in nums if nums.count(num) > 1}
# print(duplicates)


#---------------------------------------------------------------------

# def reverse_list(lst):
#     if len(lst) == 0:
#         return []
#     return [lst[-1]] + reverse_list(lst[:-1])

# print(reverse_list([1,2,3,4]))

#---------------------------------------------------------------------

# scores = {"Alice":85, "Charlie":80, "Bob":90}

# sorted_scores = dict(sorted(scores.items(), key= lambda item: item[1], reverse=True))

# print(sorted_scores)

#---------------------------------------------------------------------

# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

#---------------------------------------------------------------------

# def list_to_string(words):
#     return " ".join(words)

#---------------------------------------------------------------------

# A = {1,2,3,4}
# B = {3,4,5,6}

# print(A)
# print(B)
# print(A.symmetric_difference(B))

#---------------------------------------------------------------------

# def censor_vowels(s):
#     return "".join("*" if c in "aeiouAEIOU" else c for c in s)

#---------------------------------------------------------------------

# def reverse_words(sentence):
#     return " ".join(sentence.split()[::-1])

# print(reverse_words("Python Is Fun"))

#---------------------------------------------------------------------

# def middle_char(s):
#     mid = lens(s) // 2
#     return s[mid] if len(s) % 2 else s[mid-1:mid+1]

#---------------------------------------------------------------------

# fruits = ["apple","banana","cherry"]

# fruits.remove("banana")

# print(fruits)