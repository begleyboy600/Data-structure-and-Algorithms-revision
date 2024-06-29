"""
Quick Sort is a Divide and Conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot.
Given an array arr[], its starting position is low (the index of the array) and its ending position is high(the index of the array).

Note: The low and high are inclusive.

Implement the partition() and quickSort() functions to sort the array.

Example 1:

Input: 
N = 5 
arr[] = { 4, 1, 3, 9, 7}
Output:
1 3 4 7 9
Example 2:

Input: 
N = 9
arr[] = { 2, 1, 6, 10, 4, 1, 3, 9, 7}
Output:
1 1 2 3 4 6 7 9 10
Your Task: 
You don't need to read input or print anything. Your task is to complete the functions partition()  and quickSort() which takes the array arr[], low and high as input parameters and partitions the array. Consider the last element as the pivot such that all the elements less than(or equal to) the pivot lie before it and the elements greater than it lie after the pivot.

Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(logN)

Constraints:
1 <= N <= 103
1 <= arr[i] <= 104
"""

class Solution:
    def partition(self, arr, low, high):
        # Selecting the last element as the pivot
        pivot = arr[high]
        i = low - 1  # Index of smaller (or equal) element
        
        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        # Place the pivot element in its correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def quickSort(self, arr, low, high):
        if low < high:
            # pi is partitioning index, arr[pi] is now at right place
            pi = self.partition(arr, low, high)
            
            # Separately sort elements before partition and after partition
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)

# Main driver code
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))
        Solution().quickSort(arr, 0, n - 1)
        print(" ".join(map(str, arr)))
