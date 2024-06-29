"""
Given an array of size n-1 such that it only contains distinct integers in the range of 1 to n. Return the missing element.

Examples:

Input: n = 5, arr[] = {1,2,3,5}
Output: 4
Explanation : All the numbers from 1 to 5 are present except 4.
Input: n = 2, arr[] = {1}
Output: 2
Explanation : All the numbers from 1 to 2 are present except 2.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ n ≤ 106
1 ≤ arr[i] ≤ 106
"""
from typing import List 

class Solution:
    def missingNumber(self, n: int, arr: List[int]) -> int:
        # Calculate expected sum of first n natural numbers
        sum_expected = n * (n + 1) // 2
        
        # Calculate actual sum of elements in arr
        sum_actual = sum(arr)
        
        # Missing number is the difference
        missing_number = sum_expected - sum_actual
        
        return missing_number

# Driver code
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))
        sol = Solution()
        result = sol.missingNumber(n, arr)
        print(result)
