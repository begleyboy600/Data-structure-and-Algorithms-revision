"""
Given a non-negative integer n. The task is to check if it is a power of 2. 

Examples

Input: n = 8
Output: true
Explanation: 8 is equal to 2 raised to 3 (23 = 8).
Input: n = 98
Output: false
Explanation: 98 cannot be obtained by any power of 2.
Input: n = 1
Output: true
Explanation: (20 = 1).
Expected Time Complexity: O(log n).
Expected Auxiliary Space: O(1).

Constraints:
0 ≤ n < 1020
"""

class Solution:
    def isPowerofTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return (n & (n - 1)) == 0

# Driver code
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        sol = Solution()
        if sol.isPowerofTwo(n):
            print("true")
        else:
            print("false")
