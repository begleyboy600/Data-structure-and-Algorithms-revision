"""
Given an array arr[] of size N, check if it can be partitioned into two parts such that the sum of elements in both parts is the same.

Example 1:

Input: N = 4
arr = {1, 5, 11, 5}
Output: YES
Explanation: 
The n-queens puzzle is the problem of placing n queens on a (n×n) chessboard such that no two queens can attack each other.
Given an integer n, find all distinct solutions to the n-queens puzzle. Each solution contains distinct board configurations of the n-queens’ placement, where the solutions are a permutation of [1,2,3..n] in increasing order, here the number in the ith place denotes that the ith-column queen is placed in the row with that number. For eg below figure represents a chessboard [3 1 4 2].



 

Example 1:

Input:
1
Output:
[1]
Explaination:
Only one queen can be placed 
in the single cell available.
Example 2:

Input:
4
Output:
[2 4 1 3 ] [3 1 4 2 ]
Explaination:
These are the 2 possible solutions.
 

Your Task:
You do not need to read input or print anything. Your task is to complete the function nQueen() which takes n as input parameter and returns a list containing all the possible chessboard configurations in sorted order. Return an empty list if no solution exists.

 

Expected Time Complexity: O(n!)
Expected Auxiliary Space: O(n2) 
"""

class Solution:
    def solveNQueens(self, n):
        def is_safe(row, col, n, col_attack, diag1_attack, diag2_attack):
            return not col_attack[col] and not diag1_attack[row - col] and not diag2_attack[row + col]

        def place_queen(row, col, n, board, col_attack, diag1_attack, diag2_attack):
            board[row][col] = 'Q'
            col_attack[col] = True
            diag1_attack[row - col] = True
            diag2_attack[row + col] = True
        
        def remove_queen(row, col, n, board, col_attack, diag1_attack, diag2_attack):
            board[row][col] = '.'
            col_attack[col] = False
            diag1_attack[row - col] = False
            diag2_attack[row + col] = False

        def backtrack(row, n, board, col_attack, diag1_attack, diag2_attack, results):
            if row == n:
                results.append([''.join(row) for row in board])
                return
            
            for col in range(n):
                if is_safe(row, col, n, col_attack, diag1_attack, diag2_attack):
                    place_queen(row, col, n, board, col_attack, diag1_attack, diag2_attack)
                    backtrack(row + 1, n, board, col_attack, diag1_attack, diag2_attack, results)
                    remove_queen(row, col, n, board, col_attack, diag1_attack, diag2_attack)

        board = [['.' for _ in range(n)] for _ in range(n)]
        col_attack = [False] * n
        diag1_attack = [False] * (2 * n - 1)
        diag2_attack = [False] * (2 * n - 1)
        results = []

        backtrack(0, n, board, col_attack, diag1_attack, diag2_attack, results)
        
        return results
    
    def nQueen(self, n):
        solutions = self.solveNQueens(n)
        return solutions


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()