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

arr = [4,5,6,7,0,1,2]
target = 0
low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2
    if(arr[mid] == target):
        print(mid)
        break
    if(arr[low] <= arr[mid]):   # left half
        if arr[low] <= target < arr[mid]: # left half
            high = mid - 1
        else:
            low = mid + 1   # right half
    else:
        if arr[low] < target <= arr[high]:  # right half
            low = mid + 1
        else:
            high = mid - 1  # left half

"""

"""
1800. Maximum Ascending Subarray Sum
Easy
Given an array of positive integers nums, return the maximum possible sum of an strictly increasing subarray in nums.
A subarray is defined as a contiguous sequence of numbers in an array.

Input: nums = [12,17,15,13,10,11,12]
Output: 33
Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.

arr = [10,20,30,5,10,50]
curr_sum = max_sum = arr[0]

for i in range(1, len(arr)):
    if(arr[i] > arr[i-1]):
        curr_sum += arr[i]
    else:
        max_sum = max(max_sum, curr_sum)
        curr_sum = arr[i]
        continue

max_sum = max(max_sum, curr_sum)


print(max_sum)
"""

"""
53 - Kadane's Algorithm : Maximum Subarray Sum in an Array 

Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
has the largest sum and returns its sum and prints the subarray.

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
res = []
output = []
ptr1 = 0 
ptr2 = ptr1
curr_sum = max_sum = 0

while ptr2 >= ptr1 and ptr2 < len(arr):
    res.append(arr[ptr2])
    curr_sum += arr[ptr2]
    if(curr_sum <= 0):
        res.clear()
        ptr1 += 1
        ptr2 = ptr1
        curr_sum = 0
        continue
    if curr_sum > max_sum:
        max_sum = curr_sum
        output = [tuple(res)]  # clear previous and store new best
    elif curr_sum == max_sum and tuple(res) not in output:
        output.append(tuple(res))

    ptr2 += 1

lst = [list(l) for l in output]
print(f"max sum = {max_sum} and the subarray is = {lst}")

    Kadane's Technique

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
ptr1 = 0 
ptr2 = ptr1
curr_sum = max_sum = arr[0]

for i in range(0, len(arr)):
    curr_sum = max(arr[i], curr_sum + arr[i])
    max_sum = max(max_sum, curr_sum)


print(max_sum)

        Understanding the diff between list() and (list(l) for l in something)

output = [(4, -1, 2, 1), (4, -1, 2, 1, 0)]
print(output)

lst = [list(li) for li in output]
print(lst)   # Convert back to list if needed
longest = max(lst, key=len)
print(longest)
"""

"""
456. 132 Pattern
Medium

Given an array of n integers nums, 
a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
Return true if there is a 132 pattern in nums, otherwise, return false.

Example 1:
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Example 2:
Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
------------- Brute Force ------------
arr = [3,1,4,2]
is_132 = False

for i in range(0,len(arr)):
    for j in range(i,len(arr)):
        for k in range(j,len(arr)):
            if(arr[i] < arr[k] < arr[j]):
                is_132 = True

print(is_132)

--------------stack -------------------
arr = [3,1,4,2]
is_132 = False
stack = []
second = float('-inf')

for i in range(len(arr)-1, -1, -1):
    if(arr[i] < second):
        is_132 = True
        break
    while stack and stack[-1] < arr[i]:
        second = stack.pop()

    stack.append(arr[i])

print(is_132)
"""
"""
303. Range Sum Query - Immutable

Given an integer array nums, handle multiple queries of the following type:
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

----------- Prefix Sum -------- used when multiple queries O(n) ---------------
arr = [1,2,3,4,5]
left = 0
right = 4

pref_arr = [0] * len(arr)
pref_arr[0] = arr[0]

for i in range(1,len(pref_arr)):
    pref_arr[i] = arr[i] + pref_arr[i-1]

if left == 0:
    print(pref_arr[right])
else:
    print(pref_arr[right] - pref_arr[left-1])

--------- Brute Force ----------- used when less queries O(n)
arr = [1,2,3,4,5]
left = 0
right = 4
sum = 0

for i in range(left,right+1):
    sum += arr[i]

print(sum)
"""

"""
81. Search in Rotated Sorted Array II
Medium
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length)
Given the array nums after the rotation and an integer target,
 return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
"""
arr = [2,5,6,0,0,1,2]
target = 0
low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        found = True
        break
    if arr[mid] == arr[low] == arr[high]:
        low += 1
        high -= 1
        continue
    if arr[mid] >= arr[low]:       # at left side
        if arr[mid] > target >= arr[low]:    # confirm at left side
            high = mid - 1
        else:
            low = mid + 1
    else:       # right must be sorted
        if arr[mid] < target <= arr[high]:
            low = mid + 1
        else:
            high = mid - 1

if found:
    print("found")
else:
    print("not here")

        


         

