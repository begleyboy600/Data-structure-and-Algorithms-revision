"""
First occurrence of 5 is at index 2 and last occurrence of 5 is at index 5. 
Example 2:

Input:
n=9, x=7
arr[] = { 1, 3, 5, 5, 5, 5, 7, 123, 125 }
Output:  
6 6
Explanation: 
First and last occurrence of 7 is at index 6.
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function find() that takes array arr, integer n and integer x as parameters and returns the required answer.

Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 106
1 ≤ arr[i],x ≤ 109
"""

class Solution:
    def find(self, arr, n, x):
        # Binary search for the first occurrence of x
        def first_occurrence(arr, n, x):
            low, high = 0, n - 1
            first = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == x:
                    first = mid
                    high = mid - 1  # continue to search in the left half
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return first
        
        # Binary search for the last occurrence of x
        def last_occurrence(arr, n, x):
            low, high = 0, n - 1
            last = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == x:
                    last = mid
                    low = mid + 1  # continue to search in the right half
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return last
        
        first = first_occurrence(arr, n, x)
        last = last_occurrence(arr, n, x)
        
        return [first, last]

# { 
# Driver Code Starts
t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    n = l[0]
    x = l[1]
    arr = list(map(int, input().split()))
    ob = Solution()
    ans = ob.find(arr, n, x)
    print(*ans)
# } Driver Code Ends
