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
"""
strs = ["eat","tea","tan","ate","nat","bat"]