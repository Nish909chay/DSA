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
"""


"""
Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Examples:
Input : s = "anagram" , t = "nagaram"
Output : true
Explanation : We can rearrange the characters of string s to get string t as frequency of all characters from both strings is same.

s = "cat" 
t = "atc"
anagram = True
seen = {}
seen2 = {}

if(len(s) != len(t)):
    anagram = False
else:
    for i in s:
        seen[i] = seen.get(i,0) + 1

    for i in t:
        seen2[i] = seen2.get(i,0) + 1

    for i in seen:
        if(seen[i] != seen2.get(i,0)):
            anagram = False
            break

            OR 

if(anagram == True):
    print("valid")
else:
    print("Invalid")

from collections import Counter
s = "cat" 
t = "atca"
if(Counter(s) == Counter(t)):
    print("valid anagram")
else:
    print("invalid anagram")
"""

"""
Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import Counter
strs = ["eat","tea","tan","ate","nat","bat"]
l1 = []
l2 = []
grouped = {}


for i in strs:
    key = ''.join(sorted(i))
    if key not in grouped:
        grouped[key] = []
    grouped[key].append(i)

print(grouped)

#   OR
from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]
grouped = defaultdict(list)
for i in strs:
    key = ''.join(sorted(i))
    grouped[key].append(i)

res = grouped.values()
print(res)
"""
"""
Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

str = "ababa"
c = 0

for i in range(0,len(str)):
    for j in range(i,len(str)):
        subs = str[i:j+1]
        if subs == subs[::-1]:
                c += 1
            
print(c)

    OR

str = "ababa"
n = len(str)
c = 0

for center in range(2 * n - 1):
    left = center // 2
    right = left + (center % 2)

    while left >= 0 and right < n and str[left] == str[right]:
        c += 1
        left -= 1
        right += 1

print(c)
"""

"""
Encode and Decode Strings
You are given a list of strings, and you need to encode it into a single string (for transmission or storage), 
and then decode that string back into the original list of strings.

s = ["leet", "code", "rocks"]
# encoding
encoded = ""
for i in s:
    encoded += str(len(i)) + '#' + i

# decoding time
decoded = []
i = 0
while i < len(encoded):
    j = i
    while(encoded[j] != '#'):
        j += 1
    l = int(encoded[i:j])
    word = encoded[j+1 : j+1+l]
    decoded.append(word)
    i = j + 1 + l
    
print(decoded)
"""
"""
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character.
 You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

s = "ABAB"
k = 2
left = 0
max_len = max_freq = 0
count = {}
for r in range(len(s)):
    count[s[r]] = count.get(s[r],0) + 1
    max_freq = max(max_freq, count[s[r]])
    if((r-left+1) - max_freq) > k:
        count[s[left]] -= 1
        left += 1
    max_len = max(max_len, r - left + 1)


print(max_len)
"""
"""
409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

s = "abccccdda"
max_len = 0
found_odd = False
cnt = {}
for i in s:
    cnt[i] = cnt.get(i,0) + 1

for i in cnt.values():
    if(i%2 == 0):
        max_len += i
    else:
        max_len += i - 1
        found_odd = True

if(found_odd):
    max_len += 1

print(max_len)
"""


s = "abccccdd"
count = {}
found_odd = False
max_len = 0

for i in s:
    count[i] = count.get(i,0) + 1

for i in count.values():
    if(i % 2 == 0):
        max_len += i
    else:
        found_odd = True
        max_len += i - 1

if(found_odd):
    max_len += 1

print(max_len)


