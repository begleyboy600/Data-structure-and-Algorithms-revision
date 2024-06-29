"""
Given a value V and array coins[] of size M, the task is to make the change for V cents, given that you have an infinite supply of each of coins{coins1, coins2, ..., coinsm} valued coins. Find the minimum number of coins to make the change. If not possible to make change then return -1.


Example 1:

Input: V = 30, M = 3, coins[] = {25, 10, 5}
Output: 2
Explanation: Use one 25 cent coin
and one 5 cent coin
Example 2:
Input: V = 11, M = 4,coins[] = {9, 6, 5, 1} 
Output: 2 
Explanation: Use one 6 cent coin
and one 5 cent coin

Your Task:  
You don't need to read input or print anything. Complete the function minCoins() which takes V, M and array coins as input parameters and returns the answer.

Expected Time Complexity: O(V*M)
Expected Auxiliary Space: O(V)

Constraints:
1 ≤ V*M ≤ 106
All array elements are distinct
"""

class Solution:
    def minCoins(self, coins, M, V):
        # Initialize dp array with infinity
        dp = [float('inf')] * (V + 1)
        
        # Base case: 0 coins needed to make change for amount 0
        dp[0] = 0
        
        # Iterate through each coin
        for coin in coins:
            for j in range(coin, V + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)
        
        # If dp[V] is still infinity, return -1 (impossible case)
        if dp[V] == float('inf'):
            return -1
        else:
            return dp[V]

# Driver code
if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        V, M = map(int, input().strip().split())
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        result = ob.minCoins(coins, M, V)
        print(result)
