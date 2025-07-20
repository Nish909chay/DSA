"""
79. Word Search
Medium
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
"""
from typing import List
def exist(self, board: List[List[str]], word: str) -> bool:
    row, col = len(board), len(board[0])

    def dfs(row, col, ind):
        if ind == len(word):
            return True
        else:
            for row in range(ind, len(word)):
                for col in board[row]: