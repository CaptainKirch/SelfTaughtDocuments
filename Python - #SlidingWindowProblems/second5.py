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


# ---- PSEDUOCODE PRACTICE + SYNTAX WRITTING PRACTICE --------

#----------P1

# 1. Declare variables:
#    - window_product = product of first `k` numbers
#    - max_product = window_product

# 2. Start a for loop from `k` to `len(nums)`:
#    - Remove the element that is leaving the window by **dividing it**.
#    - Add the new element that is entering the window by **multiplying it**.

# 3. If the removed element was `0`, recalculate the product from scratch.

# 4. Update max_product to store the highest product found.

# 5. Return max_product.

from math import prod

def max_product_subarray(nums, k):
    window_product = prod(nums[:k])
    max_product = window_product


    for i in range(k, len(nums)):
        window_product += nums[i] // nums[i - k] * k
        max_product = max(max_product, window_product)


    return max_product

print(max_product_subarray([1, 5, 2, 3, 6], 2))  # Expected Output: 18 (subarray [3,6])
print(max_product_subarray([4, 3, 2, 5, 8], 3))  # Expected Output: 80 (subarray [5,8])
print(max_product_subarray([2, 1, 1, 2, 4], 2))  # Expected Output: 8 (subarray [4,2])


#----------P2

# 1. Declare variables:
#    - left = 0
#    - current_sum = 0
#    - min_length = infinity (so we can track the smallest found)

# 2. Start a for loop with `right` iterating through the array:
#    - Add `nums[right]` to `current_sum`.

# 3. Use a **while loop** inside:
#    - If `current_sum` is at least `S`:
#      - Update `min_length` to store the smallest found window.
#      - Subtract `nums[left]` from `current_sum` and move `left` forward (shrink window).

# 4. After the loop, if `min_length` was never updated, return `0`.

# 5. Otherwise, return `min_length`.

def min_length_subarray(nums, S):
    left = 0
    current_sum = 0
    min_length = float("inf")


    for right in len(nums):
        current_sum += nums[right]
        
        while current_sum < 5:
            min_length = min(min_length, current_sum)
            current_sum - nums[left] - nums[right - 1]


print(min_length_subarray([2, 3, 1, 2, 4, 3], 7))  # Expected Output: 2 ([4,3])
print(min_length_subarray([1, 2, 3, 4, 5], 11))  # Expected Output: 3 ([3,4,5])
print(min_length_subarray([1, 2, 3, 4, 5], 100))  # Expected Output: 0 (No valid subarray)

#----------P3

# 1. Declare variables:
#    - left = 0
#    - char_count = empty dictionary to store character counts
#    - max_length = 0

# 2. Start a for loop with `right` iterating through the string:
#    - Add `s[right]` to `char_count`.

# 3. If `char_count` exceeds `k` distinct characters:
#    - Shrink the window from the left:
#      - Subtract `s[left]` from `char_count` (reduce count).
#      - If count reaches `0`, remove it from dictionary.
#      - Move `left` forward.

# 4. Update `max_length` to store the longest substring found.

# 5. Return `max_length`.












# ---------P4

# 1. Declare variables:
#    - Compute `window_sum` as the sum of the first `k` numbers.
#    - min_sum = window_sum

# 2. Start a for loop from `k` to `len(nums)`:
#    - Update `window_sum` by adding `nums[i]` and subtracting `nums[i - k]` (sliding window).

# 3. Update `min_sum` with the smallest sum found.

# 4. Return `min_sum`.

# ---------P5

# 1. Declare variables:
#    - left = 0
#    - char_count = empty dictionary to count character occurrences
#    - max_length = 0

# 2. Start a for loop with `right` iterating through the string:
#    - Add `s[right]` to `char_count`.

# 3. If `char_count` contains a letter that appears less than `k` times:
#    - Shrink the window from `left` until all characters in the window appear at least `k` times.

# 4. Update `max_length` to store the longest valid substring found.

# 5. Return `max_length`.







