"""
You are given N identical eggs and you have access to a K-floored building from 1 to K.

There exists a floor f where 0 <= f <= K such that any egg dropped from a floor higher than f will break, and any egg dropped from or below floor f will not break.
There are few rules given below. 

An egg that survives a fall can be used again.
A broken egg must be discarded.
The effect of a fall is the same for all eggs.
If the egg doesn't break at a certain floor, it will not break at any floor below.
If the eggs breaks at a certain floor, it will break at any floor above.
Return the minimum number of moves that you need to determine with certainty what the value of f is.

For more description on this problem see wiki page

Example 1:

Input:
N = 1, K = 2
Output: 2
Explanation: 
1. Drop the egg from floor 1. If it 
   breaks, we know that f = 0.
2. Otherwise, drop the egg from floor 2.
   If it breaks, we know that f = 1.
3. If it does not break, then we know f = 2.
4. Hence, we need at minimum 2 moves to
   determine with certainty what the value of f is.
Example 2:

Input:
N = 2, K = 10
Output: 4
Your Task:
Complete the function eggDrop() which takes two positive integer N and K as input parameters and returns the minimum number of attempts you need in order to find the critical floor.

Expected Time Complexity : O(N*(K^2))
Expected Auxiliary Space: O(N*K)

Constraints:
1<=N<=200
1<=K<=200
"""

class Solution:
    def eggDrop(self, N, K):
        # Create a dp array with dimensions (N+1) x (K+1)
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        
        # Base cases
        for j in range(1, K + 1):
            dp[1][j] = j  # If there is only one egg, need j trials for j floors
        
        for i in range(1, N + 1):
            dp[i][0] = 0   # Zero trials for zero floors
            dp[i][1] = 1   # One trial for one floor
        
        # Fill the dp table
        for i in range(2, N + 1):
            for j in range(2, K + 1):
                dp[i][j] = float('inf')
                for x in range(1, j + 1):
                    # Calculate attempts if egg breaks or doesn't break
                    res = 1 + max(dp[i - 1][x - 1], dp[i][j - x])
                    # Take minimum of all possible attempts
                    dp[i][j] = min(dp[i][j], res)
        
        # Result is found in dp[N][K]
        return dp[N][K]

# Driver code
if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        n, k = map(int, input().strip().split())
        ob = Solution()
        print(ob.eggDrop(n, k))
