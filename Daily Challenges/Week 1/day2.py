# Day 2 Medium Python Questions and Challenges

# Question #1 --- 1️⃣ Two Sum
#Given an array of integers nums and an integer target, return the indices of the two numbers that add up to target.

# def two_sum(nums, target):




# print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]



# Question #2 --- 2️⃣ Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.


# def length_of_longest_substring(s):
    
#     current_letter = ""
#     count = 0

#     for letter in s:
#         letter = current_letter
#         if current_letter != letter:
#             count += 1

#     return count


# print(length_of_longest_substring("abcabcbb"))  # Output: 3
# print(length_of_longest_substring("bbbbb"))  # Output: 1


# Question #3 -- 3️⃣ Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements.

# from typing import Counter


# def top_k_frequent(nums, k):

#     count = Counter(nums)

# # We check how many integers in the array show up "k" number of times.

#     for key,value in count.items():
#         if count[value] == k:
#             print(count[key])

            


# # We then return those numbers that show up "k" number of times.


    

# print(top_k_frequent([1,1,1,2,2,3], 2))  # Output: [1,2]


