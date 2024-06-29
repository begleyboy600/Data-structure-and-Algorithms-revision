"""
Given two arrays of integers a[] and b[] of size n and m, the task is to check if a pair of values (one value from each array) exists such that swapping the elements of the pair will make the sum of two arrays equal.

Note: Return 1 if there exists any such pair otherwise return -1.

Example 1:

Input: n = 6, m = 4, a[] = {4, 1, 2, 1, 1, 2}, b[] = (3, 6, 3, 3)
Output: 1
Explanation: Sum of elements in a[] = 11, Sum of elements in b[] = 15, To get same sum from both arrays, we can swap following values: 1 from a[] and 3 from b[]
Example 2:

Input: n = 4, m = 4, a[] = {5, 7, 4, 6}, b[] = {1, 2, 3, 8}
Output: 1
Explanation: We can swap 6 from array a[] and 2 from array b[]
Expected Time Complexity: O(mlogm+nlogn).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ n, m ≤ 106
0 <= a[i], b[i] <= 105
"""

class Solution:
    def findSwapValues(self, a, n, b, m):
        sumA = sum(a)
        sumB = sum(b)
        
        # Calculate the difference we need to balance
        diff = sumA - sumB
        
        # If the difference is odd, no such pair can exist
        if diff % 2 != 0:
            return -1
        
        # Convert list b to set for O(1) lookup
        setB = set(b)
        
        # Iterate through array a to find the pair
        for x in a:
            y = x - diff // 2
            if y in setB:
                return 1
        
        # If no pair found
        return -1

# Driver code
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        l = list(map(int, input().split()))
        n = l[0]
        m = l[1]
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        ob = Solution()
        print(ob.findSwapValues(a, n, b, m))
