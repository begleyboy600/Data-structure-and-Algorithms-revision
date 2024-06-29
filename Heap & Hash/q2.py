"""
Given an array arr of n positive integers and an integer k, Your task is to return k largest elements in decreasing order. 

Examples

Input: arr[] = {12, 5, 787, 1, 23}, n = 5, k = 2
Output: 787 23
Explanation: 1st largest element in the array is 787 and second largest is 23.
Input: arr[] = {1, 23, 12, 9, 30, 2, 50}, n = 7, k = 3 
Output: 50 30 23
Explanation: 3 Largest element in the array are 50, 30 and 23.
Expected Time Complexity: O(k+(n-k)*logk)
Expected Auxiliary Space: O(k+(n-k)*logk)

Constraints:
1 ≤ k ≤ n ≤ 105
1 ≤ arr[i] ≤ 106
"""

import heapq

class Solution:
    def kLargest(self, arr, n, k):
        # Initialize a min-heap
        min_heap = []
        
        # Push first k elements into the heap
        for i in range(k):
            heapq.heappush(min_heap, arr[i])
        
        # Process remaining elements in the array
        for i in range(k, n):
            # If current element is larger than the root of heap, replace it
            if arr[i] > min_heap[0]:
                heapq.heapreplace(min_heap, arr[i])
        
        # Extract elements from the heap in decreasing order
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap))
        
        return result[::-1]  # Reverse to get decreasing order


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.kLargest(arr, n, k)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends