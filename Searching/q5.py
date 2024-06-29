"""
You are given an array arr[] of N integers. The task is to find the smallest positive number missing from the array.

Note: Positive number starts from 1.

Example 1:

Input:
N = 5
arr[] = {1,2,3,4,5}
Output: 6
Explanation: Smallest positive missing 
number is 6.
Example 2:

Input:
N = 5
arr[] = {0,-10,1,3,-20}
Output: 2
Explanation: Smallest positive missing 
number is 2.
Your Task:
The task is to complete the function missingNumber() which returns the smallest positive missing number in the array.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 106
-106 <= arr[i] <= 106

"""

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr, n):
        # Step 1: Segregate positive and non-positive numbers
        j = 0
        for i in range(n):
            if arr[i] <= 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
                
        # Now all non-positive numbers are to the left of index j
        # and all positive numbers are to the right of index j
        # We only care about the subarray from j to n-1
        
        # Step 2: Mark the presence of positive numbers in the range [1, n-j]
        for i in range(j, n):
            val = abs(arr[i])
            if val - 1 < n - j and arr[val - 1 + j] > 0:
                arr[val - 1 + j] = -arr[val - 1 + j]
                
        # Step 3: Find the first index which has a positive value
        for i in range(j, n):
            if arr[i] > 0:
                return i - j + 1
                
        # If all indices from j to n-1 have negative values, then the missing number is n-j+1
        return n - j + 1


# { 
# Driver Code Starts
#Initial Template for Python 3

import math


def main():
        T = int(input())
        while(T > 0):
            n = int(input())
            arr = [int(x) for x in input().strip().split()]
            ob = Solution()
            print(ob.missingNumber(arr, n))
            T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends

