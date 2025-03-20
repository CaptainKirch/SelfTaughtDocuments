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
# import math

# import math

# def dynamic_smallest(arr,x):
#     window_sum = 0
#     min_length = math.inf
#     window_start = 0

#     for window_end in range(len(arr)):
#         window_sum += arr[window_end]

#         while window_sum >= x:
#             min_length = min(min_length, window_end - window_start + 1)
#             window_sum -= arr[window_start]
#             window_start += 1

#     return min_length if min_length != math.inf else 0

# print(dynamic_smallest([2, 3, 1, 2, 4, 3], 7))
# # Output: 2 (subarray [4,3] has sum > 7)


# 4️⃣ Longest Substring with At Most K Distinct Characters
# Problem: Given a string s and an integer k, find the length of the longest substring that contains at most k distinct characters.

# import math

# def distinct_substring(s,k):
#     my_dict = {} # Dict to store frequencies.
#     window_start = 0
#     max_length = 0

#     for window_end in range(len(s)):
#         right_char = s[window_end]
#         my_dict[right_char] = my_dict.get(right_char, 0) + 1

#         while len(my_dict) > k:
#             left_char = s[window_end]
#             my_dict[left_char] -= 1
#             if my_dict[left_char] == 0:
#                 del my_dict[left_char]
#             window_start += 1
        
#     max_length = max(max_length, window_end - window_start + 1)

#     return max_length

# print(distinct_substring("araaci",2))
# # Output: 4 (longest substring "araa")




#------- question 1


# def sum_subbarray(nums,k):
#     window_sum = sum(nums[:k])
#     max_sum = window_sum

#     for i in range(k, len(nums)):
#         window_sum += nums[i] - nums[i - k]
#         max_sum = max(max_sum, window_sum)

#     return max_sum


#------- question 2

# import math

# def smallest_subarray(nums,x):
#     min_length = math.inf
#     window_start = 0
#     window_sum = 0 

#     for window_end in range(len(nums)):
#         window_sum += nums[window_end]


#         while window_sum >= x:
#             min_length = min(min_length, window_end - window_start + 1)
#             window_sum -= nums[window_start]
#             window_start += 1

#         return min_length if min_length != math.inf else 0
    

#------- question 3

# def longest_substring(s,k):
#     char_count = {}
#     window_start = 0
#     max_length = 0


#     for window_end in range(len(s)):
#         right_char = s[window_end]
#         char_count[right_char] = char_count.get(right_char, 0) + 1

#         while len(char_count) > k:
#             left_char = s[window_start]
#             char_count[left_char] -= 1
#             if char_count[left_char] == 0:
#                 del char_count[left_char]
#             window_start += 1

#     max_length = max(max_length, window_end - window_start + 1)

#     return max_length


#------- question 4

# def longest_subbstring(s,k):
#     char_count = {}
#     window_start = 0
#     max_length = 0
#     max_freq = 0

#     for window_end in range(lens(s)):
#         right_char -= s[window_end]
#         char_count[right_char] = char_count.get(right_char, 0) + 1
#         max_freq = max(max_freq, char_count[right_char])

    
#         while (window_end - window_start + 1) - max_freq > k:
#             left_char = s[window_start]
#             char_count[left_char] -= 1
#             window_start += 1

#     max_length = max(max_length, window_end - window_start + 1)

#     return max_length



# def max_subarray(nums,k):
#     window_sum = sum(nums[:k])
#     max_sum = window_sum

#     for i in range(k, len(nums)):
#         window_sum += nums[i] - nums[i - k]
#         max_sum = max(max_sum, window_sum)

#     return max_sum / k

# print(max_subarray([1, 12, -5, -6, 50, 3], 4)) 
 #-------------------------------------------------------------- 2



#-------------------------------------------------------------------3 
# import math

# def longest_str(s):
#     char_count = {}
#     window_start = 0
#     max_length = 0

#     for window_end in range(len(s)):
#         right_char = s[window_end]
#         char_count[right_char] = char_count.get(right_char, 0) + 1

#         while char_count[right_char] > 1:
#             left_char = s[window_start]
#             char_count[left_char] -= 1

#             if char_count[left_char] == 0:
#                 del left_char
#             window_start += 1

#         max_length = max(max_length, window_end - window_start + 1)

#     return max_length

# print(longest_str("abcabcbb"))
# Output: 3  # (substring "abc")


#------------------------------------------------------------------- 4
# def max_prod(nums,k):
#     window_prod = sum(nums[:k])
#     max_prod = window_prod
#     my_list = []

#     for i in range(k, len(nums)):
#         window_prod += nums[i] - nums[i - k]
#         my_list.append(window_prod * window_prod)

# def max_subarray(nums,k):
#     window_sum = sum(nums[:k])
#     max_sum = window_sum


#     for i in range(k, len(nums)):
#         window_sum += nums[i] - nums[i - k]
#         max_sum = max(max_sum, window_sum)

#     return max_sum


# print(max_subarray([2, 1, 5, 1, 3, 2],3))

# def avg_subarray(nums,k):
#     window_avg = sum(nums[:k])
#     max_length = window_avg
#     new_array = [window_avg / k]

#     for i in range(k , len(nums)):
#         window_avg += nums[i] - nums[i - k]
#         max_length =  max(max_length, window_avg)
#         new_array.append(window_avg / k)
#     return new_array
    
# print(avg_subarray([1, 3, 2, 6, -1, 4, 1, 8, 2],5))


# import math

# def smallest_subarray(nums,S):
#     min_length = math.inf
#     window_start = 0
#     window_sum = 0
    
#     for window_end in range(len(nums)):
#         window_sum += nums[window_end]

#         while window_sum >= S:
#             window_start += nums[window_start]
#             window_start += 1




