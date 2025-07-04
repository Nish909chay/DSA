"""
| Operation      | Syntax                 | Output               |
| -------------- | ---------------------- | -------------------- |
| Access         | `student["name"]`      | `"Nishchay"`         |
| Insert/Update  | `student["age"] = 22`  | age becomes 22       |
| Check key      | `"age" in student`     | True                 |
| Delete key     | `del student["grade"]` | Removes grade        |
| Get all keys   | `student.keys()`       | dict_keys([...])   |
| Get all values | `student.values()`     | dict values([...]) |
"""

"""
hashM = {
    "name" : "MnM",
    "age" : 19,
    "weight" : 68,
    "year" : "ThirdYear" 
}

print(hashM)
del hashM['name']
print(hashM)
"""

# count frequency of each number
"""
arr = [2, 3, 2, 3, 3, 5]
count = {}

for i in arr:
    if(i in count):
        count[i] += 1
    else:
        count[i] = 1

print(count)

------------- OR ---------------

arr = [2, 3, 2, 3, 3, 5]
count = {}

for i in arr:
    count[i] = count.get(i,0) + 1

print(count)
"""

"""
str = "programming"
count = {}
for i in str:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(count) 

---------------- OR ----------------

str = "prograMming"
count = {}
for i in str:
    count[i] = count.get(i,0) + 1

print(count) 
"""

# 2 SUM
"""
arr = [4,45,5,4,2,24,5,1,5]
target = 29

seen = {}

for ind,val in enumerate(arr):
    diff = target - val
    if diff in seen:
        print(f"pair found : {seen[diff]} and {ind}")
    seen[val] = ind
"""

# 2 SUM - UNIQUE PAIR COUNT - using SETS
"""arr = [3, 7, 5, 1, 9, 2, 8, 4, 6]
target = 10
seen = set()
output = set()

for val in arr:
    diff = target - val
    if diff in seen:
        output.add(tuple(sorted((val,diff))))
    seen.add(val)

print(output)
"""

"""
arr = [3, 7, 5, 1, 9, 2, 8, 4, 6]
target = 11

arr.sort(reverse=True)
print(arr)

# decreasing order 2 ptr
left = len(arr) - 1
right = 0

while right > left:
    if(arr[left] + arr[right] > target):
        right += 1
    elif(arr[left] + arr[right] < target):
        left -= 1
    else:
        print(f"pair found : {arr[left]} and {arr[right]}")
        right += 1
        left -= 1"""

"""arr = arr = [1, 2, 2, 3, 4, 5, 6]
target = 5


arr.sort(reverse=True)
print(arr)

# Two pointers on a descending array
left = len(arr) - 1
right = 0

while left > right:
    current_sum = arr[left] + arr[right]
    if current_sum > target:
        right += 1  # move to smaller sum (go to smaller element)
    elif current_sum < target:
        left -= 1  # need bigger sum (go to larger element)
    else:
        print(f"Pair found: {arr[left]} and {arr[right]}")
        right += 1
        left -= 1"""

"""
238. Product of Array Except Self
Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
# Brute Force
arr = [1,2,3,4]

arr2 = [0] * len(arr)
for ptr1 in range(len(arr)):
    prod = 1                # reset
    for ptr2 in range(len(arr)):
        if(ptr1 == ptr2):
            continue
        prod *= arr[ptr2]
    arr2[ptr1] = prod
print(arr2)

# Optimized 
arr = [1,0,3,4]
left = [0] * len(arr)
right = [0] * len(arr)
res_arr = [0] * len(arr)


left[0] = 1
for i in range(1,len(arr)):
    left[i] = left[i - 1] * arr[i - 1]

right[len(arr) - 1] = 1
for i in range(len(arr) - 2, -1, -1):
    right[i] = right[i + 1] * arr[i + 1]
 

for i in range(len(res_arr)):
    res_arr[i] = left[i] * right[i]

print(res_arr)
"""
    
"""
Check Balanced Parentheses. 
Given string str containing just the characters '(', ')', '{', '}', '[' and ']', 
check if the input string is valid and return true if the string is balanced otherwise return false.

str = "([{}]))"
stack = [] 
valid = True

for i in str:
    if(i == '(' or i == '{' or i == '['):
        stack.append(i)
    if(i == ')' or i == '}' or i == ']'):
        if not stack:
            valid = False
            break
        top = stack.pop()
        if(i == '}' and top != '{'):
            valid = False
            break
        elif(i == ')' and top != '('):
            valid = False
            break
        elif(i == ']' and top != '['):
            valid = False
            break


if(valid == True):
    print("valid parenthesis")
else:
    print("invalid parenthesis")

    OR

str = "([{}][)"

pmap = {')':'(', ']':'[', '}': '{'}

stack = []
valid = True
 
for i in str:
    if i in "({[":
        stack.append(i)
    elif i in ")}]":
        if not stack:
            valid = False
            break

        if(pmap[i] != stack.pop()):
            valid = False
            break



if(valid == True):
    print("valid parenthesis")
else:
    print("invalid parenthesis")

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

"""
153. Find Minimum in Rotated Sorted Array
Medium
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

nums = [3,4,5,0,1,2]
low = 0
high = len(nums) - 1
while low < high:
    mid = int((low + high) / 2)
    if(nums[high] < nums[mid]):
        low = mid + 1
    elif(nums[high] > nums[mid]):
        high = mid 

print(nums[low])
"""

"""
33. Search in Rotated Sorted Array
Medium

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

nums = [4,5,6,7,0,1,2]
target = 0
low = 0
high = len(nums) - 1
while low < high:
    mid = int((low + high) / 2)
    if(nums[mid] == target):
        print(mid)
    
    if(nums[mid] > nums[low]):
        if(nums[low] <= target < nums[mid]):
            high = mid - 1
        else:
            low = mid + 1
    
    else:
        if(nums[mid] < target < )
DOUBT
"""

"""
3 Sum : Find triplets that add up to a zero
Example 1: 

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

Explanation: Out of all possible unique triplets possible, [-1,-1,2] and [-1,0,1] satisfy the condition of summing up to zero with i!=j!=k

Example 2:

Input: nums=[-1,0,1,0]
Output: Output: [[-1,0,1],[-1,1,0]]
Explanation: Out of all possible unique triplets possible, [-1,0,1] and [-1,1,0] satisfy the condition of summing up to zero with i!=j!=k

arr = [-1,0,1,2,-1,-4]
target = 0
res = set()
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            sum = arr[i] + arr[j] + arr[k]
            if(sum == 0):
                res.add(tuple(sorted((arr[i],arr[j],arr[k]))))

        
ls = [list(t) for t in res]
print(ls)


best approach

arr = [-4, -1, -1, 0, 1, 2]
arr.sort()
res = set()

for i in range(0,len(arr) - 3):
    left = i + 1
    right = len(arr) - 1
    if(i > 0 and arr[i] == arr[i-1]):
        continue
    while(left < right):    
        sum = arr[left] + arr[right] + arr[i]
        if(sum == 0 ):
            res.add(tuple(sorted((arr[left], arr[right], arr[i]))))
            while(left < right and arr[left] == arr[left + 1]):
                left += 1
            while(left < right and arr[right] == arr[right - 1]):
                right -= 1
            left += 1
            right -= 1
        elif(sum > 0):
            right -= 1
        else:
            left += 1

print(res)
"""




    

