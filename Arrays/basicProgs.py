"""
LIST: 




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

