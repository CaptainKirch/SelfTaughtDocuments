#Questions Number 1 -- Problem: Find the length of the longest substring without repeating characters.

# PC -- 
# 1.  Create a set to track unique characters.
# 2. Use two pointers(left, right)
# 3. Expand right, adding unique characters.
# 4. If duplicate appears, remove from left until its unique again.
# 5. Update max length.

def length_of_longest_substring(s):
    letter_set = set()
    left = 0 
    max_length = 0

    for right in range(len(s)):
        while s[right] in letter_set: 
            letter_set.remove(s[left])
            left += 1

        letter_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

print(length_of_longest_substring("abcabcbb"))  # Output: 3  ("abc")
print(length_of_longest_substring("bbbbb"))  # Output: 1  ("b")
print(length_of_longest_substring("pwwkew"))  # Output: 3  ("wke")
print(length_of_longest_substring("abcdef"))  # Output: 6  ("abcdef")
print(length_of_longest_substring(""))  # Output: 0 (empty string)

#Questions Number 2 -- Problem: Find the maximum sum of any contiguous subarray of size "k".

# PC -- 
# 1. Initalize window sum and max sum using the first K element.
# 2. Expand the window by adding the next element and removing the first.
# 3. After reaching K, slide the window by shifting left pointer.
# 4. Update max sum at each step.

def max_sum_subarray(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum =  max(max_sum, window_sum)

    return max_sum

print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # Output: 9 ([5, 1, 3])
print(max_sum_subarray([1, 2, 3, 4, 5, 6], 2))  # Output: 11 ([5, 6])
print(max_sum_subarray([4, -1, 2, 1], 2))  # Output: 5 ([4, 1])
print(max_sum_subarray([5, -3, 5, -2, 5], 3))  # Output: 8 ([5, -2, 5])


#Questions Number 3 -- Problem: Given a string and an integer k, find the longest substring where you can replace at most k characters to make all characters the same.

# PC -- 
# 1. Use two pointers (left, right) to track the window.
# 2. Expand right and track character frequencies.
# 3. If window size - max frquencty > k, shrink window.
# 4. Update max length when expanding.

from collections import Counter

def character_replacement(s, k):
    count = Counter()
    left = 0
    max_freq = 0
    max_length = 0

    for right in range(len(s)):
        count[s[right]] += 1
        max_freq = max(max_freq, count[s[right]])

    if (right - left + 1) - max_freq > k:
        count[s[left]] -= 1
        left += 1

    max_length - max(max_length, right - left + 1)

    return max_length

print(character_replacement("AABABBA", 1))  # Output: 4 ("AABA" or "BABB")
print(character_replacement("ABAB", 2))  # Output: 4 ("ABAB" or "BABA")
print(character_replacement("AAAA", 2))  # Output: 4 ("AAAA")
print(character_replacement("AABAA", 1))  # Output: 5 ("AABAA")
print(character_replacement("ABCD", 1))  # Output: 2 ("AA" or "BB", etc.)



#Questions Number 4 -- Problem: Given two strings s1 and s2, check if any permutation of s1 exists in s2.

# PC -- 
# 1. Use character counts for s1.
# 2. Maintain a window of size len(s1) in s2.
# 3. If window count match s1 count, return True.
# 4. Otherwise, slide window.

from collections import Counter

def check_inclusion(s1, s2):
    s1_count = Counter(s1)
    window_count = Counter(s2[:len(s1)])

    if s1_count == window_count:
        return True
    
    for i in range(len(s1), len(s2)):
        window_count[s2[i]] += 1
        window_count[s2[i - len(s1)]] -= 1

        if window_count[s2[i - len(s1)]] == 0:
            del window_count[s2[i - len(s1)]]
        if window_count == s1_count:
            return True
    return False

print(check_inclusion("ab", "eidbaooo"))  # Output: True ("ba" is in "eidbaooo")
print(check_inclusion("ab", "eidboaoo"))  # Output: False (no "ab" permutation)
print(check_inclusion("adc", "dcda"))  # Output: True ("cda" is a permutation)
print(check_inclusion("hello", "ooolleoooleh"))  # Output: False



#Questions Number 5 --  Problem: Find the smallest substring in "s" that contains all characters of "t".

# PC -- 
# 1. Use two pointers (left, right)
# 2. Track character frequencies.
# 3. Expand right to include t's characters.
# 3. Once valid, shrink left while maintaining validity.
# 4. Otherwise, slide window.

from collections import Counter

def min_window(s, t):
    if not t or not s:
        return ""

    t_count = Counter(t)
    window_count = {}
    left, min_length = 0, float("inf")
    result = ""

    for right, char in enumerate(s):
        window_count[char] = window_count.get(char, 0) + 1

        while all(window_count.get(c, 0) >= t_count[c] for c in t_count):
            if right - left + 1 < min_length:
                min_length = right - left + 1
                result = s[left:right+1]
            window_count[s[left]] -= 1
            left += 1

    return result

print(min_window("ADOBECODEBANC", "ABC"))  # Output: "BANC"
print(min_window("a", "a"))  # Output: "a"
print(min_window("a", "aa"))  # Output: "" (not possible)
print(min_window("aab", "ab"))  # Output: "ab"


