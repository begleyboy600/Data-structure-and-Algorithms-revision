"""
Given a 2D grid of n*m of characters and a word, find all occurrences of given word in grid. A word can be matched in all 8 directions at any point. Word is said to be found in a direction if all characters match in this direction (not in zig-zag form). The 8 directions are, horizontally left, horizontally right, vertically up, vertically down, and 4 diagonal directions.

Note: The returning list should be lexicographically smallest. If the word can be found in multiple directions starting from the same coordinates, the list should contain the coordinates only once. 

Example 1:

Input: 
grid = {{a,b,c},{d,r,f},{g,h,i}},
word = "abc"
Output: 
{{0,0}}
Explanation: 
From (0,0) we can find "abc" in horizontally right direction.
Example 2:

Input: 
grid = {{a,b,a,b},{a,b,e,b},{e,b,e,b}}
word = "abe"
Output: 
{{0,0},{0,2},{1,0}}
Explanation: 
From (0,0) we can find "abe" in right-down diagonal. 
From (0,2) we can find "abe" in left-down diagonal. 
From (1,0) we can find "abe" in horizontally right direction.
Your Task:
You don't need to read or print anything, Your task is to complete the function searchWord() which takes grid and word as input parameters and returns a list containing the positions from where the word originates in any direction. If there is no such position then returns an empty list.

Expected Time Complexity: O(n*m*k) where k is constant
Expected Space Complexity: O(1)

Constraints:
1 <= n <= m <= 50
1 <= |word| <= 15
"""

class Solution:
    def searchWord(self, grid, word):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),  # up, down, left, right
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]  # diagonal directions
        
        n = len(grid)
        m = len(grid[0])
        len_word = len(word)
        found_positions = set()
        
        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < m
        
        def search_from(x, y):
            for dir_x, dir_y in directions:
                nx, ny = x, y
                match = True
                for k in range(len_word):
                    if not is_valid(nx, ny) or grid[nx][ny] != word[k]:
                        match = False
                        break
                    nx += dir_x
                    ny += dir_y
                if match:
                    found_positions.add((x, y))
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == word[0]:
                    search_from(i, j)
        
        return sorted(list(found_positions))

# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n); m = int(m);
        grid = []
        for _ in range(n):
            cur = input()
            temp = []
            for __ in cur:
                temp.append(__)
            grid.append(temp)
        word = input()
        obj = Solution()
        ans = obj.searchWord(grid, word)
        for _ in ans:
            for __ in _:
                print(__, end=" ")
            print()
        if len(ans) == 0:
            print(-1)
# Driver Code Ends
