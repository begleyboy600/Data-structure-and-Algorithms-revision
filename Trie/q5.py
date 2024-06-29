"""
Given an array of integers of size N find minimum xor of any 2 elements.


Example 1:

Input:
N = 3
arr[] = {9,5,3}
Output: 6
Explanation: 
There are 3 pairs -
9^5 = 12
5^3 = 6
9^3 = 10
Therefore output is 6.

Your Task:  
You don't need to read input or print anything. Your task is to complete the function minxorpair() which takes the array arr[], its size N as input parameters and returns the minimum value of xor of any 2 elements.

 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

 

Constraints:
1 <= N <= 105
1 <= arr[i] <= 105
"""

class Solution:
    def minxorpair(self, N, arr):
        arr.sort()  # Step 1: Sort the array
        
        min_xor = float('inf')
        
        # Step 2: Compute XOR of adjacent elements and track minimum
        for i in range(N - 1):
            xor_val = arr[i] ^ arr[i + 1]
            if xor_val < min_xor:
                min_xor = xor_val
        
        return min_xor


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
    
        ob = Solution()
        print(ob.minxorpair(N,arr))
        

# } Driver Code Ends