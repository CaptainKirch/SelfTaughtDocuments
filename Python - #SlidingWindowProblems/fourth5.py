# ___________ Question 1

# def max_summer(nums,k):
#     window_sum = sum(nums[:k])
#     max_sum = window_sum

#     for i in range(k, len(nums)):
#         window_sum += nums[i] - nums[i - k]
#         max_sum = max(max_sum, window_sum)

#     return max_sum

# print(max_summer([2, 1, 5, 1, 3, 2],3))


# ___________ Question 2

# def avg_subarray(nums,k):
#     window_sum = sum(nums[:k])
#     max_sum = window_sum
#     new_array = []

#     for i in range(k, len(nums)):
#         new_array.append(window_sum / k)
#         window_sum += nums[i] - nums[i - k]
    
#     return new_array

# print(avg_subarray([1, 3, 2, 6, -1, 4, 1, 8, 2],5))  



# ___________ Question 3

# import math

# def smallest_subarray(nums, target):
#     min_length = math.inf
#     current_sum = 0
#     left = 0

#     for right in range(len(nums)):
#         current_sum += nums[right]

#         while current_sum >= target:
#             min_length = min(min_length, right - left + 1)
#             current_sum -= nums[left]
#             left += 1
            
#     return min_length if min_length != float('inf') else 0

# print(smallest_subarray([2, 1, 5, 2, 3, 2], 7))

# # ___________ Question 4

# def count_ana(s, p):
#     from collections import Counter

#     # Step 1: Initialize
#     window_start = 0
#     match_count = 0
#     char_count = Counter(p)  # Store frequency of characters in p
#     window_size = len(p)
#     result = 0

#     # Step 2: Iterate through s with sliding window
#     for window_end in range(len(s)):
#         right_char = s[window_end]

#         if right_char in char_count:
#             char_count[right_char] -= 1
#             if char_count[right_char] == 0:
#                 match_count += 1

#         # Shrink window if it gets larger than `p`
#         if window_end >= window_size - 1:
#             if match_count == len(char_count):
#                 result += 1  # Found an anagram

#             left_char = s[window_start]
#             if left_char in char_count:
#                 if char_count[left_char] == 0:
#                     match_count -= 1
#                 char_count[left_char] += 1
#             window_start += 1

#     return result

# # Test Case
# print(count_ana("cbaebabacd", "abc"))  # Output: 2


# # ___________ Question 5

# def maximum_sum(nums):
#     max_sum = float('-inf')

#     for i in range(len(nums) - 1):  # Prevent out-of-bounds error
#         current_sum = nums[i] + nums[i + 1]
#         max_sum = max(max_sum, current_sum)

#     return max_sum

# # Test Case
# print(maximum_sum([4, 2, 1, 7, 3, 6]))  # Output: 10


# # ___________ Question 7 (medium)

# def longest_substring(s,k):
#     print("Function started")

#     char_count = {}
#     max_length = 0
#     left = 0


#     for right in range(len(s)):
#         right_char = s[right]
#         char_count[right_char] = char_count.get(right_char, 0) + 1













