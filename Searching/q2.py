"""
Given an integer x, find the square root of x. If x is not a perfect square, then return floor(√x).

 

Example 1:

Input:
x = 5
Output: 2
Explanation: Since, 5 is not a perfect 
square, floor of square_root of 5 is 2.
Example 2:

Input:
x = 4
Output: 2
Explanation: Since, 4 is a perfect 
square, so its square root is 2.
 

Your Task:
You don't need to read input or print anything. The task is to complete the function floorSqrt() which takes x as the input parameter and return its square root.
Note: Try Solving the question without using the sqrt function. The value of x>=0.

 

Expected Time Complexity: O(log N)
Expected Auxiliary Space: O(1)

 

Constraints:
1 ≤ x ≤ 107
"""

class Solution:
    def floorSqrt(self, x): 
        # Your code here
        if x == 0 or x == 1:
            return x
        
        low, high, ans = 0, x, 0
        
        while low <= high:
            mid = (low + high) // 2
            
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
                ans = mid  # update answer as we need the floor value
            else:
                high = mid - 1
        
        return ans

# { 
# Driver Code Starts
# Initial Template for Python 3

import math

def main():
        T = int(input())
        while T > 0:
            x = int(input())
            print(Solution().floorSqrt(x))
            T -= 1

if __name__ == "__main__":
    main()
# } Driver Code Ends
