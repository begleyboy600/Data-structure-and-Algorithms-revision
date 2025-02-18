"""
Stickler the thief wants to loot money from a society having n houses in a single line. He is a weird person and follows a certain rule when looting the houses. According to the rule, he will never loot two consecutive houses. At the same time, he wants to maximize the amount he loots. The thief knows which house has what amount of money but is unable to come up with an optimal looting strategy. He asks for your help to find the maximum money he can get if he strictly follows the rule. ith house has a[i] amount of money present in it.

Example 1:

Input:
n = 5
a[] = {6,5,5,7,4}
Output: 
15
Explanation: 
Maximum amount he can get by looting 1st, 3rd and 5th house. Which is 6+5+4=15.
Example 2:

Input:
n = 3
a[] = {1,5,3}
Output: 
5
Explanation: 
Loot only 2nd house and get maximum amount of 5.
Your Task:
Complete the functionFindMaxSum() which takes an array arr[] and n as input which returns the maximum money he can get following the rules.

Expected Time Complexity:O(N).
Expected Space Complexity:O(1).

Constraints:
1 ≤ n ≤ 105
1 ≤ a[i] ≤ 104
"""

class Solution:
    def FindMaxSum(self, a, n):
        if n == 0:
            return 0
        if n == 1:
            return a[0]
        
        dp = [0] * (n + 1)
        dp[1] = a[0]
        
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], a[i - 1] + dp[i - 2])
        
        return dp[n]

# Driver Code
if __name__ == '__main__':
    test_cases = int(input().strip())
    for _ in range(test_cases):
        n = int(input().strip())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.FindMaxSum(a, n))
