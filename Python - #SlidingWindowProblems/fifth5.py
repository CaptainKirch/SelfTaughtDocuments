# Given a string s and an integer k, find the length of the longest substring that contains at most k distinct characters.

# def longest_substring(s,k):
#     char_count = {}
#     max_length = 0
#     left = 0

#     for window_end in range(len(s)):
#         right_char = s[window_end]
#         char_count[right_char] = char_count.get(right_char, 0) + 1

#         while len(char_count) > k:
#             left_char = s[left]
#             char_count[left_char] -= 1
#             if char_count[left_char] == 0:
#                 del char_count[left_char]
#             left += 1

#         max_length = max(max_length, window_end - left + 1)

#     return max_length

# s = "araaci"
# k = 2
# 4  # The longest substring is "araa"



# Given an array of positive integers nums and an integer target, find the length of the smallest contiguous subarray whose sum is greater than or equal to target. If no such subarray exists, return 0.


# import math

# def smallest_subarray(nums,target):
#     min_length = math.inf
#     left = 0
#     current_sum = 0

#     for right in range(len(nums)):
#         current_sum += nums[right]
        

#         while current_sum >= target:
#             min_length = min(min_length, right - left +1)
#             current_sum -= nums[left]
#             left += 1
            
            
#     return 0 if min_length == math.inf else min_length
