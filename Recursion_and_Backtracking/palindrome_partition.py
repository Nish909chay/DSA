"""
131. Palindrome Partitioning
Medium
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
"""
from typing import List 

def partition(self, s: str) -> List[List[str]]:
    res = []

    def backtrack(start, path: List[int]):
        if(start == len(s)):
            res.append(path[:])
            return
        else:
            for end in range(start, len(s)):
                substr = s[start : end + 1]
                if(substr == substr[::-1]):
                    path.append(substr)
                    backtrack(end+1, path)
                    path.pop()

    backtrack(0,[])
    return res


