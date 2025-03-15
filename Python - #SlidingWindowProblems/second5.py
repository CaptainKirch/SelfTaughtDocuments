# Day 2 - Sliding Window Problems Challenge Questions - Writing PseduoCode and Syntax

# Problem 1 - Given an integer array nums and an integer k, return the maximum sum of any contiguous subarray of size k.

# Problem In My Own Words -  The problem is asking to review a given array of integers and a given single interger in the function. We are being asked to figure out the maximum sum of any contiguous subarray that is of the size "k".

# def max_sum_subarray(nums, k):

#     window_sum = sum(nums[:k])
#     max_sum = window_sum

#     for i in range(k, len(nums)):

#         window_sum += nums[i] - nums[i - k]

#         max_sum = max(max_sum, window_sum)

#     return max_sum 

# print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # Output: 9 (subarray [5,1,3])
# print(max_sum_subarray([1, 9, 3, 7, 2], 2))  # Output: 12 (subarray [9,3])


# Problem 2 - Given an integer array nums and an integer S, find the length of the smallest contiguous subarray whose sum is at least S.

# Problem In My Own Words - This question is asking for us to check the array that is provided and use sliding window through the array and find the smallest subarray which a sum of atleast 5.


#Intitalize Variables.

# Expand the window ( right moves forward):

# Add nums[right] to current)sum

#Shrink the window (left moves forward)

# If current_sum >= S, check if the window is the smallest so far.

# Subtract nums[left] from current_sum and move left forward.


# Return min_length if valid subarray was found, otherwise return 0.

# def min_subarray_length(nums, S):

#     left = 0 # This vairable is starting the window.
#     current_sum = 0 # Running sum of elements in window.
#     min_length = float("inf") # Store the smallest valid subarray (the answer)

#     # Expand the window by moving 'right'
#     for right in range(len(nums)):
#         current_sum += nums[right] # This adds the current number to the window sum.

#         # While current sum is at least S, try to minimize the window.
#         while current_sum >= S:
#             min_length = min(min_length, right - left + 1) # Update min length
#             current_sum -= nums[left] #Remove leftmost element
#             left += 1 #Move left pointer forward.


#         #If no valid subarray found, return 0
#     return min_length if min_length != float("inf") else 0 


# print(min_subarray_length([2, 3, 1, 2, 4, 3], 7))  # Output: 2 ([4,3])
# print(min_subarray_length([1, 2, 3, 4, 5], 11))  # Output: 3 ([3,4,5])
# print(min_subarray_length([1, 2, 3, 4, 5], 100))  # Output: 0 (No valid subarray)


# Problem 3 - Given an array of positive integers nums and an integer k, find the maximum product of any contiguous subarray of size k.

# from math import prod

# def max_product_subarray(nums, k):
#     window_product = prod(nums[:k])
#     max_product = window_product

#     for i in range(k, len(nums)):
#         if nums [i - k] != 0:
#             window_product = (window_product // nums[i - k] * nums[i])
#         else:
#             window_product = prod(nums[i-k+1:i+1])

#         max_product = max(max_product, window_product)
    
#     return max_product

# print(max_product_subarray([1, 5, 2, 3, 6], 2))  # Output: 18 (subarray [3,6])
# print(max_product_subarray([4, 3, 2, 5, 8], 3))  # Output: 80 (subarray [2,5,8])
# print(max_product_subarray([2, 1, 1, 2, 4], 2))  # Output: 8 (subarray [2,4])


# Problem 3 - Given an array of integers nums and an integer k, find the minimum sum of any contiguous subarray of size k.

# def min_sum_subarray(nums, k):

#     window_sum = sum(nums[:k])
#     min_sum = window_sum

#     for i in range(k, len(nums)):
#         window_sum += nums[i] - nums[i - k]
#         min_sum = min(min_sum, window_sum)

#     return min_sum

# print(min_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # Output: 6 (subarray [1,3,2])
# print(min_sum_subarray([4, 3, 2, 5, 8], 2))  # Output: 5 (subarray [3,2])
# print(min_sum_subarray([10, 20, 30, 40, 50], 3))  # Output: 60 (subarray [10,20,30])









