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

def min_subarray_length(nums, S):

    left = 0 # This vairable is starting the window.
    current_sum = 0 # Running sum of elements in window.
    min_length = float("inf") # Store the smallest valid subarray (the answer)


    # Expand the window by moving 'right':

    for right in range(len(nums)):
        current_sum += nums[right] # This adds the current number to the window sum.

        # While current sum is at least S, try to minimize the window.
        while current_sum >= S:
            min_length = min(min_length, right - left + 1) # Update min length

















print(min_subarray_length([2, 3, 1, 2, 4, 3], 7))  # Output: 2 ([4,3])
print(min_subarray_length([1, 2, 3, 4, 5], 11))  # Output: 3 ([3,4,5])
print(min_subarray_length([1, 2, 3, 4, 5], 100))  # Output: 0 (No valid subarray)










