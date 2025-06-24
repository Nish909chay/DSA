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

