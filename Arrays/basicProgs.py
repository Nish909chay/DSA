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
print("Max product subarray:", max_prod)

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
"""

"""
1. Check if a Number is Prime

import math
n = 21
is_prime = True
if(n <= 1):
    is_prime =  False
else:
    for i in range(2,n):        if optimize - int(math.sqrt(n))
        if(n%i == 0):
            is_prime =  False
            break
        


if(is_prime):
    print("Prime")
else:
    print("Not Prime")
"""

"""
Generate Fibonacci Series

r = 10
arr = [0] * r
arr[0] = 0
arr[1] = 1

for i in range(2,r):
    arr[i] = arr[i-1] + arr[i-2]
    
print(arr)
"""

"""
Swap Two Numbers Without Using a Temporary Variable

a = 5
b = 16
a = a ^ b
b = a ^ b
a = a ^ b

print(f"a = {a}, b = {b}")

# or

a = 21
b = 16
a = a + b
b = a - b
a = a - b

print(f"a = {a}, b = {b}")
"""

"""
Count the Number of Digits in an Integer

n = 15
digits = [int(d) for d in str(n)]
print(len(digits))
"""
"""
5. Find Duplicate Numbers in a List  +  optimized
arr = [1,2,1,1,5,2,4,8,7,5]
seen = {}
alr_printed = set()
for i in arr:
    if i in seen:
        if i not in alr_printed:
            print(f"duplicate number : {i}")
            alr_printed.add(i) 
    seen[i] = seen.get(i,0) + 1
"""

"""
6. Find Unique (Non-Duplicate) Numbers in a List

arr = [1,2,1,1,5,2,4,8,7,5]
arr2 = [0] * len(arr)
seen = {}
for i in arr:
    seen[i] = seen.get(i,0) + 1

for i in seen:
    if seen[i] == 1:
        print(f"unique = {i}", end=" ")
    else:
        continue
"""
"""
Find the first unique number

arr = [1,2,1,1,5,2,4,8,7,5]

seen = {}
for i in arr:
    seen[i] = seen.get(i,0) + 1
for i in arr:
    if seen[i] == 1:
        print(f"unique = {i}", end=" ")
        break
    else:
        continue
"""

"""
First non-repeating character in a string?

str = "Nishchay"
seen = {}
for i in str:
    seen[i] = seen.get(i,0) + 1

for i in str:
    if(seen[i] == 1):
        print(f"First non repeating char : {i}")
        break
"""

"""
9. Find the Smallest Number in a List
10. Find the Largest Number in a List

arr = [1,2,1,1,5,2,4,8,7,5]
mx = max(arr)
mn = min(arr)
print(f"MAX = {mx} and MIN = {mn}")
"""
"""
7. Calculate the Factorial of a Number
n = 11      # 39916800
fact = 1
for i in range(1,n+1):
    fact *= i

print(fact)
"""

"""
11. Calculate the Sum of Digits of a Number

n = 12345
arr = [int(d) for d in str(n)]

sum = 0
for i in arr:
    sum += i

print(sum)
# or
n = 123456
sum = 0
while n > 0:
    sum += n % 10
    n //= 10
print(sum)

"""

"""
13. Check if a Number is a Palindrome

n = 123321
arr = [int(d) for d in str(n)]

ptr1 = 0
ptr2 = len(arr) - 1
is_palindrome = True

while ptr1 < ptr2:
    if(arr[ptr1] != arr[ptr2]):
        is_palindrome = False
        break
    else:
        ptr1 += 1
        ptr2 -= 1

print(is_palindrome)
"""

"""
12. Check if a Number is an Armstrong Number

n = 9474
exp = len(str(n))
arr = [int(d) for d in str(n)]
sum = 0

for i in arr:
    sum += i ** exp

if(sum == n):
    print(f"{sum} is arm strong")
else:
    print(f"{sum} is not arm strong")
"""

"""
8. Reverse a Number

n = 123
arr = [int(d) for d in str(n)]
for i in range(len(arr)-1, -1, -1):
    print(arr[i],end="")

# oR

n = 123
rev = 0
while n > 0:
    dig = n % 10
    rev = rev * 10 + dig
    n //= 10

print(rev)
"""

"""print Prime Numbers upto range
-------- Brute Force --------
n = 20

for i in range(2,n):
    is_prime = True
    for j in range(2,i):
        if(i%j == 0):
            is_prime = False
    if(is_prime):
        print(i)

----------------- Optimized - O(n log log n) --------------
n = 20
prime_list = [True] * (n+1)
prime_list[0] = prime_list[1] = False

for i in range(2,int(n**0.5) + 1):
    if prime_list[i]:
        for j in range(i*i, n + 1, i):
            prime_list[j] = False 

for i in range(n + 1):
    if(prime_list[i]):
        print(i, end = " ")

"""
"""
                iska output bata
-----------------
arr = [1,2,3]
arr.append([4,5])
print(len(arr))
--------------
a = [1, 2, 3]
a = tuple(a)
a[0] = 2
print(a)
-------------------
a = [1, 2]
print(a * 3)

word = "PythonProgramming"
print(len(word))
"""
str = "abaa"
print(str.count('a'))