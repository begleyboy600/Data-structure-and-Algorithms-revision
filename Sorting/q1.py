"""
Given an array arr[] and an integer k where k is smaller than the size of the array, the task is to find the kth smallest element in the given array. It is given that all array elements are distinct.

Note:-  l and r denotes the starting and ending index of the array.

Example 1:

Input:
n = 6
arr[] = 7 10 4 3 20 15
k = 3
l=0 r=5

Output : 
7

Explanation :
3rd smallest element in the given 
array is 7.
Example 2:

Input:
n = 5
arr[] = 7 10 4 20 15
k = 4 
l=0 r=4

Output : 
15

Explanation :
4th smallest element in the given 
array is 15.
Your Task:
You don't have to read input or print anything. Your task is to complete the function kthSmallest() which takes the array arr[], integers l and r denoting the starting and ending index of the array and an integer k as input and returns the kth smallest element.
 
Expected Time Complexity: O(n*log(n) )
Expected Auxiliary Space: O(log(n))
Constraints:
1 <= n <= 105
l = 0
r = N-1
1<= arr[i] <= 105
1 <= k <= n
"""

class Solution:
    def kthSmallest(self, arr, l, r, k):
        if k > 0 and k <= r - l + 1:
            # Partition the array around last element
            pivot_index = self.partition(arr, l, r)
            
            # If pivot itself is the k-th smallest element
            if pivot_index - l == k - 1:
                return arr[pivot_index]
            
            # If pivot is greater, recur left subarray
            if pivot_index - l > k - 1:
                return self.kthSmallest(arr, l, pivot_index - 1, k)
            
            # Else recur right subarray
            return self.kthSmallest(arr, pivot_index + 1, r, k - pivot_index + l - 1)
        
        # If k is out of range
        return float('inf')
    
    def partition(self, arr, l, r):
        # Choosing the last element as pivot
        pivot = arr[r]
        i = l - 1
        
        for j in range(l, r):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[r] = arr[r], arr[i + 1]
        return i + 1
