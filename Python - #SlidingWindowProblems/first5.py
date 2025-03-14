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

# Step 1:
# This problem is asking us to look at a list of numbers that are provided and check if we can see any numbers that are totalling "S" which is an integer that will be given in the function. We need to make sure its the smallest amount of numbers that it takes to total the "S" int.


# Step 2:
# 1. Create variables for left and right.
# 2. For loop over the array and check if the numbers of the left side are totalling to "S". And check on the right side are the numbers totalling to "S".
# 3. Return a newly created list of those totalling to the function.


#---------------------------------------------------------------------------

# #Problem 4 --  Problem:
# Find the longest substring containing at most k distinct characters.

# Step 1:
# This problem is asking us to check the string that is provided to us for the most "k" characters that are in a certain subtring in the string.


# Step 2:
# 1. We would create a variable for "Counter" and import it into the code.
# 2. We would create a for loop over the string and use the counter to check how many counts of each unique variable there is.
# 3. We would then create an if statement inside the for loop that if the counter was equal to "k" number of times for a certain letter we would then stop the loop and then print what the indexed letters were in that substring.

#---------------------------------------------------------------------------

# #Problem 5 --  Problem:
# You are given a list of fruits, where each fruit is represented by an integer. You can carry at most 2 types of fruits at a time. Find the maximum number of fruits you can pick up in a row.

# Step 1:
# Unknown
# Step 2:
# Unkown


















