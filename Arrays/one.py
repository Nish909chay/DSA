"""| Operation        | Python Code          | Result                    |
| ---------------- | -------------------- | ------------------------- |
| Access element   | `arr[0]`             | First element             |
| Update element   | `arr[1] = 10`        | Sets second element to 10 |
| Add at end       | `arr.append(6)`      | Adds 6 at the end         |
| Insert at index  | `arr.insert(2, 100)` | Inserts 100 at index 2    |
| Remove by value  | `arr.remove(3)`      | Removes first `3`         |
| Remove last item | `arr.pop()`          | Removes last item         |
| Remove at index  | `arr.pop(2)`         | Removes item at index 2   |
| Length of array  | `len(arr)`           | Returns size of list      |
| Check membership | `3 in arr`           | True/False                |
| Sort             | `arr.sort()`         | Sorts in-place ascending  |
| Reverse          | `arr.reverse()`      | Reverses in-place         |
"""
"""
enumrate()
arr = [1,4,7,'str1','str2']

for index,data in enumerate(arr):
    print(data,index)"""
# 2 SUM

"""arr=[4,5,6,2,1,15,9]
target = 20


arr.sort()
left = 0
right = len(arr) - 1;

while left < right:
    if((arr[left] + arr[right]) > target):
        right -= 1
    elif(arr[left] + arr[right] < target):
        left += 1
    else:
        print(f"pair : {arr[left]} and {arr[right]}")
        break"""


# LCM
"""import math
a = 12
b= 18
max_num = max(a,b)
print("jkf")

while True:
    if (max_num % a == 0) and (max_num % b == 0):
        lcm = max_num
        break
    max_num += 1

print(f"LCM is {lcm} ")"""

"""
# HCF
a = 12
b= 18
min_num = min(a,b)

while True:
    if (a % min_num == 0) and (b % min_num == 0):
        hcf = min_num
        break
    min_num -= 1

print(f"HCF is {hcf} ")"""

# subarray sum equals K using Brute Force
"""arr = [5,3,8,1,2,1]
c = 0
k = 4
for i in range(len(arr)):
    sum = 0
    for j in range(i,len(arr)):
        sum += arr[j]
        if(sum == k):
            c+=1
print(f"count = {c}")"""

# using hash map
"""arr = [5,3,8,1,2,1]
k = 4
ln = len(arr)
pref_arr = [0] * len(arr) + 1
for val in range(1,len(arr)):
    pref_arr[val] = pref_arr[val-1] + arr[val]
seen = {0: 1}
c = 0
for val in range(1, ln + 1):
    curr = pref_arr[val]
    target = curr - k
    if target in seen:
        c += seen[target]       # occurence 
    seen[curr] = seen.get(curr,0) + 1"""


# Maximum Product Subarray in an Array
"""arr = [1,2,-3,0,-4,-5]
# arr =  [1,2,3,4,5,0]
n = len(arr)

left_pref = [0] * n
right_pref = [0] * n

max_left = max_right = 0

# Left-to-right pass WITHOUT reset
prod = 1
for i in range(n):
    prod *= arr[i]
    left_pref[i] = prod
    max_left = max(max_left, prod)

# Right-to-left pass WITHOUT reset
prod = 1
for i in range(n - 1, -1, -1):
    prod *= arr[i]
    right_pref[i] = prod
    max_right = max(max_right, prod)

# Final result
max_prod = max(max_left, max_right)
print("Max product subarray:", max_prod)"""

#arr = [1,2,-3,0,-4,-5]
"""arr =  [1,2,3,4,5,0]
left_pref = [0] * len(arr)
right_pref = [0] * len(arr)
max_left = max_right = 0

prod = 1
for ind in range(len(arr)):
    prod *= arr[ind]
    left_pref[ind] = prod 
    max_left = max(max_left, prod)

prod = 1
for ind in range(len(arr) - 1, -1, -1):
    prod *= arr[ind]
    right_pref[ind] = prod
    max_right = max(max_right, prod)

# Final result
max_prod = max(max_left, max_right)
print("Max product subarray:", max_prod)"""

#optimizing this
arr =  [1,2,3,4,5,0]
#arr = [1,2,-3,0,-4,-5]
curr_max = curr_min = 1
max_prod = arr[0]

for val in arr:
    if(val == 0):
        curr_max = curr_min = 1
        max_prod = max(max_prod, 0)
        continue

    prod = curr_max * val
    curr_max = max(val, prod, curr_min * val)
    curr_min = min(val, prod, curr_min * val)
    max_prod = max(curr_max, max_prod)

print(max_prod)




