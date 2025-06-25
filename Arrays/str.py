"""
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

str = "abcfabcbb"
left = right = 0
MAX = 0
seen = set()

while (right < len(str)):
    if str[right] not in seen:
        seen.add(str[right])
        MAX = max(MAX, (right-left + 1))
        right += 1
    else:
        seen.remove(str[left])
        left += 1
print(MAX)
"""
"""
424. Longest Repeating Character Replacement
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
"""
str = "AABABBA"
k = 1
seen = {}
left = 0
max_freq = max_len = 0

for right in range(len(str)):
    seen[str[right]] = seen.get(str[right],0) + 1
    max_freq = max(max_freq, seen[str[right]])
    
    # check if window size and changed char greater than k
    if(((right - left) + 1) - max_freq) > k:
        seen[str[left]] -= 1
        left += 1
    
    max_len = max(max_len, (right - left + 1))

print(max_len)









    

