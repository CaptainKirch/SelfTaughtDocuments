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


# def longest_subarray(nums,target):
#     max_length = 0
#     left = 0
#     current_sum = 0
    
#     for right in range(len(nums)):
#         current_sum += nums[right]

#         while current_sum > target:
#             current_sum -= nums[left]
#             left += 1
        
#         max_length = max(max_length, right - left + 1)
#     return max_length


# def longest_substring(s):
#     max_length = 0
#     char_count = {}
#     left = 0

#     for right in range(len(s)):
#         char_count[s[right]] = char_count.get(s[right], 0 ) + 1

#         while char_count[s[right]] > 1:
#             char_count[s[left]] -= 1
#             if char_count[s[left]] == 0:
#                 del char_count[s[left]]
#             left += 1

#         max_length = max(max_length, right - left + 1)
        
#     return max_length


# Given an array of integers nums and an integer k, find the maximum sum of any contiguous subarray of size k.

# def maximum_sum(nums,k):
#     window_sum = sum(nums[:k])
#     max_sum = window_sum

#     for i in range(k, len(nums)):
#         window_sum = window_sum + nums[i] - nums[i - k]
    
#         max_sum = max(max_sum, window_sum)

#     return max_sum

# print(maximum_sum([2, 1, 5, 1, 3, 2],3))



# Given a string s, return the length of the longest substring without repeating characters.


# def longest_substring(s):
#     max_length = 0
#     left = 0
#     char_count = {}

#     for right in range(len(s)):
#         right_char = s[right]
#         char_count[right_char] = char_count.get(right_char, 0) + 1

#         while char_count[s[right]] > 1:
#             char_count[s[left]] -= 1
#             if char_count[s[left]] == 0:
#                 del char_count[s[left]]  # Remove if count is zero
#             left += 1 
        
#         max_length = max(max_length, right - left + 1)

#     return max_length

# print(longest_substring("abcabcbb"), "abc")


# Given a string s and an integer k, return the length of the longest substring that contains at most k distinct characters.

# def long_substring(s,k):
#     max_length = 0
#     left = 0
#     char_count = {}

#     for right in range(len(s)):
#         right_char = s[right]
#         char_count[right_char] = char_count.get(right_char, 0) + 1


#     while len(char_count) > k:
#         char_count[s[left]] -= 1
#         if char_count[s[left]] == 0:
#             del char_count[s[left]]
#         left += 1

#         max_length = max(max_length, right - left + 1)

#     return max_length

# print(long_substring("araaci",2))






















