"""
LIST: 
1. Check if a Number is Prime
2. Generate Fibonacci Series
3. Swap Two Numbers Without Using a Temporary Variable
4. Count the Number of Digits in an Integer
5. Find Duplicate Numbers in a List
6. Find Unique (Non-Duplicate) Numbers in a List
7. Calculate the Factorial of a Number
8. Reverse a Number
9. Find the Smallest Number in a List
10. Find the Largest Number in a List
11. Calculate the Sum of Digits of a Number
12. Check if a Number is an Armstrong Number
13. Check if a Number is a Palindrome
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
"""
r = 10
arr = [0] * r
arr[0] = 0
arr[1] = 1

for i in range(2,r):
    arr[i] = arr[i-1] + arr[i-2]
    
print(arr)