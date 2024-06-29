"""
Given a sorted and rotated array arr of n distinct elements which may be rotated at some point, and given an element key, the task is to find the index of the given element key in the array arr. The whole array arr is given as the range to search.

Rotation shifts elements of the array by a certain number of positions, with elements that fall off one end reappearing at the other end.

Note:- 0-based index is followed & return -1 if the key is not present.

Examples :

Input: n = 9, arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3}, key = 10
Output: 5
Explanation: 10 is found at index 5.
Input: n = 4, arr[] = {3, 5, 1, 2}, key = 6
Output: -1
Explanation:  There is no element that has value 6.
Expected Time Complexity: O(log n).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ n ≤ 107
0 ≤ arr[i] ≤ 108
1 ≤ key ≤ 108
"""

class Solution:
    def search(self, n, arr, key):
        # Helper function to find the pivot
        def find_pivot(arr, low, high):
            if high < low:
                return -1
            if high == low:
                return low

            mid = (low + high) // 2

            if mid < high and arr[mid] > arr[mid + 1]:
                return mid
            if mid > low and arr[mid] < arr[mid - 1]:
                return mid - 1
            if arr[low] >= arr[mid]:
                return find_pivot(arr, low, mid - 1)
            return find_pivot(arr, mid + 1, high)

        # Helper function to perform binary search
        def binary_search(arr, low, high, key):
            if high < low:
                return -1
            mid = (low + high) // 2

            if key == arr[mid]:
                return mid
            if key > arr[mid]:
                return binary_search(arr, mid + 1, high, key)
            return binary_search(arr, low, mid - 1, key)

        # Finding the pivot
        pivot = find_pivot(arr, 0, n - 1)

        # If no pivot is found, the array is not rotated
        if pivot == -1:
            return binary_search(arr, 0, n - 1, key)

        # If pivot is found, compare with key and search in the two subarrays
        if arr[pivot] == key:
            return pivot
        if arr[0] <= key:
            return binary_search(arr, 0, pivot - 1, key)
        return binary_search(arr, pivot + 1, n - 1, key)

# { 
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        k = int(input())
        ob = Solution()
        print(ob.search(n, A, k))

# } Driver Code Ends
