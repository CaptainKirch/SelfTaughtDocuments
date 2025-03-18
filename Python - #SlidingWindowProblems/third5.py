# Sliding Window Easy Problem 1: “Given an array of integers and a number ‘k,’ find the maximum average of any contiguous subarray of size ‘k’.”

def fixed_window(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum / k

print(fixed_window([1, 12, -5, -6, 50, 3],4))


# Sliding Window Easy Problem 2: “Given an array of positive integers and a target ‘S,’ find the length of the longest contiguous subarray whose sum is less than or equal to ‘S’. Return 0 if no such subarray exists.”

def dynamic_wind(arr,S):
    




# arr = [4, 3, 1, 2, 5, 1, 6]
# S = 7