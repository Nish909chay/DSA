"""
338. Counting Bits
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

n = 5
arr = [0] * (n + 1)

for ind in range(len(arr)):
    arr[ind] = bin(ind).count('1')

print(arr)
"""

"""
3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest substring without duplicate characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""
str = "abcdabcbb"
seen = set()
left = right = 0
c = 0
max_len = 0

while right < len(str):
    if str[right] not in seen:
        seen.add(str[right])
        max_len = max(max_len, (right - left) + 1)
        right += 1
    else:
        seen.remove(str[left])
        left += 1
    
print(max_len)

        

    
