"""
The two parts are {1, 5, 5} and {11}.
Example 2:

Input: N = 3
arr = {1, 3, 5}
Output: NO
Explanation: This array can never be 
partitioned into two such parts.
Your Task:
You do not need to read input or print anything. Your task is to complete the function equalPartition() which takes the value N and the array as input parameters and returns 1 if the partition is possible. Otherwise, returns 0.

Expected Time Complexity: O(N*sum of elements)
Expected Auxiliary Space: O(sum of elements)

Constraints:
1 ≤ N ≤ 100
1 ≤ arr[i] ≤ 1000
N*sum of elements ≤ 5*106
"""

class Solution:
    def equalPartition(self, N, arr):
        total_sum = sum(arr)
        
        # If total sum is odd, cannot partition into two equal subsets
        if total_sum % 2 != 0:
            return 0
        
        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in arr:
            # Update dp array from right to left to avoid overwriting
            for j in range(target, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True
        
        return 1 if dp[target] else 0


import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")