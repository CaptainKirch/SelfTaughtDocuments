# Day 1 - Sliding Window Problems Challenge Questions

#---------------------------------------------------------------------------

#Problem 1 -- Problem:
# Given an array nums and an integer k, find the maximum average of any contiguous subarray of size k.

# Step 1:
#  This questions is asking for you to take the array/list of numbers that is provided in the function and the number k, and then add up the numbers in "k" index places in the list and then find the average of those numbers and then return that average to the function.


# Step 2:
# 1. Create a variable that will hold the average of the numbers that will be added up and returned to the function.
# 2. Create a for loop over the array for the certain index spaces.
# 3. Add up each iterable with one another when the for loop is going over the array.
# 4. Once adding up is completed divide that number by the total number of indexes that was iterated over, in otherwords "k" and return that in a variable to the function.

#---------------------------------------------------------------------------

#Problem 2 --  Problem:
# Given a string s and a pattern p, find how many times any permutation of p appears in s.

# Step 1:
# This problem is asking for the return of all the anagrams in a string that show up.

#Step 2:
# 1. Create a variable that represents "p" in reverse, so that we have a variables of both forward and reversed.

# 2.We then want to for loop over the string and see if the combination of letters that are in reversed "p" and forward "p" are present.

# 3.If the anagrams are present we want to add them into a new list that is created with just those anagrams. 


#---------------------------------------------------------------------------

#Problem 3 --  Problem:
# Find the smallest contiguous subarray length where the sum is at least S. Return 0 if no valid subarray exists.


def min_subarray_length(nums, S):

# Step 1:
# This problem is asking us to look at a list of numbers that are provided and check if we can see any numbers that are totalling "S" which is an integer that will be given in the function. We need to make sure its the smallest amount of numbers that it takes to total the "S" int.


# Step 2:
# 1. 



print(min_subarray_length([2,3,1,2,4,3], 7))  # Output: 2 ([4,3])
print(min_subarray_length([1,1,1,1,1,1,1], 5))  # Output: 5 ([1,1,1,1,1])
print(min_subarray_length([1,2,3,4,5], 11))  # Output: 3 ([3,4,5])






