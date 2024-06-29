"""
Given two unsorted arrays arr1[] and arr2[]. They may contain duplicates. For each element in arr1[] count elements less than or equal to it in array arr2[].

Example 1:

Input:
m = 6, n = 6
arr1[] = {1,2,3,4,7,9}
arr2[] = {0,1,2,1,1,4}
Output: 4 5 5 6 6 6
Explanation: Number of elements less than
or equal to 1, 2, 3, 4, 7, and 9 in the
second array are respectively 4,5,5,6,6,6
Example 2:

Input:
m = 5, n = 7
arr1[] = {4,8,7,5,1}
arr2[] = {4,48,3,0,1,1,5}
Output: 5 6 6 6 3
Explanation: Number of elements less than
or equal to 4, 8, 7, 5, and 1 in the
second array are respectively 5,6,6,6,3
Your Task :
Complete the function countEleLessThanOrEqual() that takes two array arr1[], arr2[],  m, and n as input and returns an array containing the required results(the count of elements less than or equal to it in arr2 for each element in arr1 where ith output represents the count for ith element in arr1.)

Expected Time Complexity: O(M logN + N logN).
Expected Auxiliary Space: O(m).

Constraints:
1<=m,n<=10^5
0<=arr1[i],arr2[j]<=10^5 
"""

from bisect import bisect_right

class Solution:
    def countEleLessThanOrEqual(self, arr1, n1, arr2, n2):
        # Sort the second array
        arr2.sort()
        
        result = []
        # For each element in arr1, find the count of elements less than or equal to it in arr2
        for num in arr1:
            count = bisect_right(arr2, num)
            result.append(count)
        
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n1, n2 = [int(x) for x in input().split()]
        arr1 = [int(x) for x in input().split()]
        arr2 = [int(x) for x in input().split()]
    
        res = Solution().countEleLessThanOrEqual(arr1, n1, arr2, n2)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
# } Driver Code Ends
