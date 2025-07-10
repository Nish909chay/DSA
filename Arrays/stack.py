
"""
155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(self.min_stack[-1], val))
            
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.min_stack[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
"""
"""
232. Implement Queue using Stacks

Implement a first in first out (FIFO) queue using only two stacks.
 The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)
        
    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop()) 
        return self.stack2.pop()
        
    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
        
    def empty(self):
        return not self.stack1 and not self.stack2
"""
"""
17. Letter Combinations of a Phone Number
Medium

Given a string containing digits from 2-9 inclusive,
 return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
    DOUBT
"""

"""
496. Next Greater Element I
Easy
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. 
If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
---------- Brute force ------
nums1 = [4,1,2]
nums2 = [1,3,4,2]
output = []
found = False

for i in range(len(nums1)):
    for j in range(len(nums2)):
        if(nums1[i] == nums2[j]):
            found = False
            for k in range(j+1,len(nums2)):
                if(nums1[i] < nums2[k]):
                    output.append(nums2[k])
                    found = True
                    break
            if(found != True):
                output.append(-1)
            break


print(output)

----------- Stack -----------------

nums1 = [4,1,2]
nums2 = [1,3,4,2]
output = []
stack = []
memory = {}

# monotonic decreasing stack (if asked greater - mononotic decreasig ) and (if asked smaller - monotonic increasing)
stack.append(nums2[0])
for i in range(1,len(nums2)):
    if(stack and stack[-1] > nums2[i]):
        stack.append(nums2[i])
    else:
        while(stack and stack[-1] < nums2[i]):
            val = stack.pop()
            memory[val] = nums2[i]
        stack.append(nums2[i])

while stack:
    memory[stack.pop()] = -1 

for i in range(len(nums1)):
    if nums1[i] in memory:
        output.append(memory[nums1[i]])
    else:
        output.append(-1)

print(output)

"""
"""
739. Daily Temperatures
Medium

Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
 If there is no future day for which this is possible, keep answer[i] == 0 instead.

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
    

temp = [73,74,75,71,69,72,76,73]
stack = []
output= [0] * len(temp)
stack.append(0)

for i in range(1, len(temp)):
    if(stack and temp[stack[-1]] > temp[i]):
        stack.append(i)
    else:
        while(stack and temp[stack[-1]] < temp[i]):
            val = stack.pop()   # returns the index 
            output[val] = (i - val)
        stack.append(i)

print(output)
"""

"""
901. Online Stock Span
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward)
for which the stock price was less than or equal to the price of that day.

Example 1:

Input
[[], [100], [80], [60], [70], [60], [75], [85]]
Output
[null, 1, 1, 1, 2, 1, 4, 6]

"""
arr = [100, 80, 60, 70, 60, 75, 85]
span = [0] * len(arr)
stack = []

for i in range(len(arr)):
    while(stack and arr[stack[-1]] <= arr[i]):
        stack.pop()
    if not stack:
        span[i] = i + 1
    else:
        span[i] = i - stack[-1]
    stack.append(i)
            
    
print(span)





    



