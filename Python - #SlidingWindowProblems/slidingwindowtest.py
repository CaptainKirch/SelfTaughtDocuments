#1 Fixed
# Given an array of positive numbers and a positive number 'k,' find the maximum sum of any contiguous subarray of size 'k'.

# def maximum_subarray(nums,k):
#     window_sum = sum(nums[:k])
#     max_sum = window_sum


#     for i in range(k,len(nums)):
#         window_sum += nums[i] - nums[i -k]
#         max_sum = max(max_sum, window_sum)

#     return max_sum

# print(maximum_subarray([2, 1, 5, 1, 3, 2],3))


#2 Dynamic
# Given an array of positive integers and a number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to 'S'. Return 0 if no such subarray exists.

# import math

# def smallest_subarray(arr,S):
#     min_length = math.inf
#     window_start = 0
#     window_sum = 0

#     for window_end in range(len(arr)):
#         window_sum += arr[window_end]

#         while window_sum >= S:
#             max_length = min(min_length, window_end - window_start + 1)
#             window_sum -= arr[window_start]
#             window_start += 1
        
#     min_length == math.inf:
#         return 0
        
#     return min_length

# print(smallest_subarray([2, 1, 5, 2, 3, 2],7))


#3 - Hash Map + Dynamic
# Given a string, find the length of the longest substring in it with no more than K distinct characters. You can assume that K is less than or equal to the length of the given string.

# def longest_substring(str1,k):
#     max_length = 0
#     window_start = 0
#     char_frequency = {}

#     for window_end in range(len(str1)):
#         right_char = str1[window_end]
#         if right_char not in char_frequency:
#             char_frequency[right_char] = 0

#         while len(char_frequency) > k:
#             left_char = str1[window_start]
#             if char_frequency[left_char] == 0:
#                 del char_frequency[left_char]
#             window_start += 1

#         max_length = max(max_length, window_end - window_start + 1)

#     return max_length
        
# print(longest_substring("araaci",2))


# 4 - Hash Map + Dynamic
# You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets. You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions: 
# Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
# You can start with any tree, but you can’t skip a tree once you have started.
# You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
# Write a function to return the maximum number of fruits in both baskets.

# def fruits_basket(fruits):
#     max_length = 0
#     window_start = 0
#     fruits_frequency = {}

#     for window_end in range(len(fruits)):
#         right_fruits = fruits[window_end]
#         if right_fruits not in fruits_frequency:
#             fruits_frequency[right_fruits] = 0
#         fruits_frequency[right_fruits] += 1


#         while len(fruits_frequency) > 2:
#             left_fruits = fruits[window_start]
#             fruits_frequency[left_fruits] -= 1
#             if fruits_frequency[left_fruits] == 0:
#                 del fruits_frequency[left_fruits]
#             window_start += 1

#         max_length = max(max_length, window_end - window_start + 1)
#     return max_length
        

# print(fruits_basket(['A', 'B', 'C', 'A', 'C']))



