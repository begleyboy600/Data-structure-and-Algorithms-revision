"""
Given two sorted arrays array1 and array2 of size m and n respectively. Find the median of the two sorted arrays.

Example 1:

Input:
m = 3, n = 4
array1[] = {1,5,9}
array2[] = {2,3,6,7}
Output: 5
Explanation: The middle element for
{1,2,3,5,6,7,9} is 5
Example 2:

Input:
m = 2, n = 4
array1[] = {4,6}
array2[] = {1,2,3,5}
Output: 3.5
Your Task:
The task is to complete the function MedianOfArrays() that takes array1 and array2 as input and returns their median. 

Can you solve the problem in expected time complexity?

Expected Time Complexity: O(min(log n, log m)).
Expected Auxiliary Space: O((n+m)/2).

Constraints: 
0 ≤ m,n ≤ 106
1 ≤ array1[i], array2[i] ≤ 109
"""

class Solution:
    def findMedianSortedArrays(self, array1, array2):
        if len(array1) > len(array2):
            array1, array2 = array2, array1
        
        m, n = len(array1), len(array2)
        left, right = 0, m
        total_len = m + n
        
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (total_len + 1) // 2 - partition1
            
            max_left1 = float('-inf') if partition1 == 0 else array1[partition1 - 1]
            min_right1 = float('inf') if partition1 == m else array1[partition1]
            
            max_left2 = float('-inf') if partition2 == 0 else array2[partition2 - 1]
            min_right2 = float('inf') if partition2 == n else array2[partition2]
            
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if total_len % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
                else:
                    return float(max(max_left1, max_left2))
            elif max_left1 > min_right2:
                right = partition1 - 1
            else:
                left = partition1 + 1
        
        # If we reach here, arrays are not sorted or valid, though as per problem constraints it should always return.
        raise ValueError("Arrays are not sorted or valid.")
