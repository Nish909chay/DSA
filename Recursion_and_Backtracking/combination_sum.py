"""
39. Combination Sum
Medium
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times.
 Two combinations are unique if the frequency of at least one of the chosen numbers is different.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
"""
from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def backtrack(start, current: List[int], totalsum):
        if(totalsum == target):
            result.append(current[:])       # store a copy
            return
        elif(totalsum > target):
            return
        else:
            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, totalsum + candidates[i])
                candidates.pop()

    backtrack(0, [], 0)
    return result
