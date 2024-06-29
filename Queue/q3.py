"""
Given a grid of dimension nxm where each cell in the grid can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cells have fresh oranges
2 : Cells have rotten oranges

We have to determine what is the earliest time after which all the oranges are rotten. A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time. 
 

Example 1:

Input: grid = {{0,1,2},{0,1,2},{2,1,1}}
Output: 1
Explanation: The grid is-
0 1 2
0 1 2
2 1 1
Oranges at positions (0,2), (1,2), (2,0)
will rot oranges at (0,1), (1,1), (2,2) and 
(2,1) in unit time.
Example 2:

Input: grid = {{2,2,0,1}}
Output: -1
Explanation: The grid is-
2 2 0 1
Oranges at (0,0) and (0,1) can't rot orange at
(0,3).
 

Your Task:
You don't need to read or print anything, Your task is to complete the function orangesRotting() which takes grid as input parameter and returns the minimum time to rot all the fresh oranges. If not possible returns -1.
 

Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)
 

Constraints:
1 ≤ n, m ≤ 500
"""

from collections import deque

class Solution:
    def orangesRotting(self, grid):
        if not grid:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        
        # Directions for up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        queue = deque()
        fresh_count = 0
        
        # Initialize the queue with all initially rotten oranges
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))  # (row, col, time)
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0  # No fresh oranges to rot
        
        time = 0
        
        while queue:
            i, j, time = queue.popleft()
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                    grid[ni][nj] = 2  # Mark as rotten
                    fresh_count -= 1
                    queue.append((ni, nj, time + 1))
        
        if fresh_count == 0:
            return time
        else:
            return -1  # Some oranges couldn't be rotted

# Driver Code
if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    index = 1
    for _ in range(T):
        n, m = map(int, data[index].split())
        index += 1
        grid = []
        for i in range(n):
            row = list(map(int, data[index].split()))
            grid.append(row)
            index += 1
        
        # Create an object of Solution class
        sol = Solution()
        # Compute and print the minimum time to rot all oranges
        print(sol.orangesRotting(grid))
