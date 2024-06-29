"""
Given an array arr[] of n integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.

Examples:

Input: arr[] = {1,2,3,-2,5}, n = 5
Output: 9
Explanation: Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.
Input: arr[] = {-1,-2,-3,-4}, n = 4
Output: -1
Explanation: Max subarray sum is -1 of element (-1)
Input: arr[] = {5,4,7}, n = 3
Output: 16
Explanation: Max subarray sum is 16 of element (5, 4, 7)
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
-107 ≤ arr[i] ≤ 107
1 ≤ n ≤ 106
"""

def maxSubArraySum(arr, n):
    max_so_far = arr[0]
    max_ending_here = arr[0]

    for i in range(1, n):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far


if __name__ == "__main__":
    arr1 = [1, 2, 3, -2, 5]
    n1 = len(arr1)
    print(maxSubArraySum(arr1, n1))  # Output: 9

    arr2 = [-1, -2, -3, -4]
    n2 = len(arr2)
    print(maxSubArraySum(arr2, n2))  # Output: -1

    arr3 = [5, 4, 7]
    n3 = len(arr3)
    print(maxSubArraySum(arr3, n3))  # Output: 16
