"""
Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell.

Example 1:

Input:
N = 4
m[][] = {{1, 0, 0, 0},
         {1, 1, 0, 1}, 
         {1, 1, 0, 0},
         {0, 1, 1, 1}}
Output:
DDRDRR DRDDRR
Explanation:
The rat can reach the destination at 
(3, 3) from (0, 0) by two paths - DRDDRR 
and DDRDRR, when printed in sorted order 
we get DDRDRR DRDDRR.
Example 2:
Input:
N = 2
m[][] = {{1, 0},
         {1, 0}}
Output:
-1
Explanation:
No path exists and destination cell is 
blocked.
Your Task:  
You don't need to read input or print anything. Complete the function printPath() which takes N and 2D array m[ ][ ] as input parameters and returns the list of paths in lexicographically increasing order. 
Note: In case of no path, return an empty list. The driver will output "-1" automatically.

Expected Time Complexity: O((3N^2)).
Expected Auxiliary Space: O(L * X), L = length of the path, X = number of paths.

Constraints:
2 ≤ N ≤ 5
0 ≤ m[i][j] ≤ 1
"""

class Solution:
    def findPath(self, m, n):
        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < n and m[x][y] == 1 and not visited[x][y]
        
        def backtrack(x, y, path):
            if x == n-1 and y == n-1:
                result.append(''.join(path))
                return
            
            for direction in directions:
                nx, ny = x + direction[0], y + direction[1]
                if is_valid(nx, ny):
                    visited[nx][ny] = True
                    path.append(direction_to_char[direction])
                    backtrack(nx, ny, path)
                    path.pop()
                    visited[nx][ny] = False
        
        if m[0][0] == 0 or m[n-1][n-1] == 0:
            return []
        
        visited = [[False] * n for _ in range(n)]
        result = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        direction_to_char = {(-1, 0): 'U', (1, 0): 'D', (0, -1): 'L', (0, 1): 'R'}
        
        visited[0][0] = True
        backtrack(0, 0, [])
        
        return sorted(result)

# Driver code
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))
        matrix = [arr[i*n:(i+1)*n] for i in range(n)]
        obj = Solution()
        result = obj.findPath(matrix, n)
        if not result:
            print(-1)
        else:
            for path in result:
                print(path, end=" ")
            print()
