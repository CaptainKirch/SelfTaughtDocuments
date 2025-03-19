# # Sliding Window Easy Problem 1: “Given an array of integers and a number ‘k,’ find the maximum average of any contiguous subarray of size ‘k’.”

# def fixed_window(arr, k):
#     window_sum = sum(arr[:k])
#     max_sum = window_sum

#     for i in range(k, len(arr)):
#         window_sum += arr[i] - arr[i - k]
#         max_sum = max(max_sum, window_sum)

#     return max_sum / k

# print(fixed_window([1, 12, -5, -6, 50, 3],4))


# # Sliding Window Easy Problem 2: “Given an array of positive integers and a target ‘S,’ find the length of the longest contiguous subarray whose sum is less than or equal to ‘S’. Return 0 if no such subarray exists.”

# def longest_subarray_with_sum_at_most(arr, S):
#     window_sum = 0
#     max_length = 0  # Track longest subarray
#     window_start = 0

#     for window_end in range(len(arr)):
#         window_sum += arr[window_end]  # Expand window

#         # If sum exceeds S, shrink from left
#         while window_sum > S:
#             window_sum -= arr[window_start]
#             window_start += 1
        
#         # Update longest subarray length
#         max_length = max(max_length, window_end - window_start + 1)

#     return max_length  # Return 0 if no valid subarray exists

# print(longest_subarray_with_sum_at_most([4, 3, 1, 2, 5, 1, 6], 7))  # Output: 4


# 🟢 Easy Sliding Window Problems (Fixed Window)

# 1️⃣ Maximum Sum Subarray of Size K ------------- Problem: Given an array of integers nums and an integer k, find the maximum sum of any contiguous subarray of size k.

# def array_sum(arr,k):
#     window_sum = sum(arr[:k])
#     max_sum = window_sum


#     for i in range(k, len(arr)):
#         window_sum += arr[i] - arr[i - k]
#         max_sum = max(max_sum, window_sum)

#     return max_sum 


# print(array_sum([2, 1, 5, 1, 3, 2],3))
# # 9 (subarray [5, 1, 3] has the max sum)


# 2️⃣ Average of Subarrays of Size K -------------- Problem: Given an array nums and a number k, return an array containing the average of all subarrays of size k.

# def avg_array(arr,k):
#     window_avg = sum(arr[:k])

#     avg_list = [window_avg / k]

#     for i in range(k, len(arr)):
#         window_avg += arr[i] - arr[i - k]
#         avg_list.append(window_avg / k)

#     return avg_list

# print(avg_array([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
# Output: [2.2, 2.8, 2.4, 3.6, 2.8]

# 🟢 Easy Sliding Window Problems (Dynamic Window)

# 3️⃣ Smallest Subarray with Sum Greater Than X
# Problem: Given an array of positive integers nums and an integer x, find the smallest contiguous subarray whose sum is greater than x.





# Input: nums = [2, 3, 1, 2, 4, 3], x = 7
# Output: 2 (subarray [4,3] has sum > 7)











# 4️⃣ Longest Substring with At Most K Distinct Characters
# Problem: Given a string s and an integer k, find the length of the longest substring that contains at most k distinct characters.







# Input: s = "araaci", k = 2
# Output: 4 (longest substring "araa")










# 5️⃣ Longest Repeating Character Replacement
# Problem: Given a string s and an integer k, find the length of the longest substring where you can replace up to k characters to make all characters the same.










# Input: s = "AABABBA", k = 1
# Output: 4 (Change "BABB" to "AAAA")