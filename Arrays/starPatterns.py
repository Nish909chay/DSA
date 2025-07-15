#square pattern
"""for i in range(4):
    for j in range(3):
        print("*", end="")
    print()

***
***
***
***

"""

# Right-Angled Triangle
"""
*
**
***
****

for i in range(5):
    for j in range(i):
        print("*", end="")
    print()"""

"""
Inverted Triangle
****
***
**
*

for i in range(5,-1,-1):
    for j in range(i):
        print("*", end="")
    print()
"""

"""
Right-Aligned Triangle
   *
  **
 ***
****

n = 5
for i in range(n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(i):
        print("*", end = "")
    print()
"""

"""
Pyramid

   *
  ***
 *****
*******

n = 4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i - 1):
        print("*", end = "")
    print()
"""
"""
Inverted Pyramid
*******
 *****
  ***
   *

n = 4
for i in range(n, -1, -1):
    for j in range(i, n):
        print(" ", end="")
    for k in range((2*i - 1),0, -1):
        print("*", end = "")
"""

"""
Diamond
   *
  ***
 *****
  ***
   *

n = 4
for i in range(1,n+1):
    for j in range((n-i)):
        print(" ",end="")
    for k in range(2*i-1):
        print("*", end="")
    print()
#inverted
for i in range(n-1,0, -1):
    for j in range(i,n):
        print(" ",end="")
    for k in range((2*i-1),0,-1):
        print("*", end="")
    print()
"""

"""
Hollow Square
*****
*   *
*   *
*****

n = 5
for i in range(1,n):
    if(i==1 or i==n):
        print("*" * n)
    else:
        print("*" + " " * (n-2) + "*")
"""

n = 4

for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()

for i in range(n-1, 0, -1):
    for j in range(i, n):
        print(" ",end = "")
    for k in range(2*i-1,0, -1):
        print("*", end = "")
    print()