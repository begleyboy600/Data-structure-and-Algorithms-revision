"""
Given two integer arrays A1[ ] and A2[ ] of size N and M respectively. Sort the first array A1[ ] such that all the relative positions of the elements in the first array are the same as the elements in the second array A2[ ].
See example for better understanding.
Note: If elements are repeated in the second array, consider their first occurance only.

Example 1:

Input:
N = 11 
M = 4
A1[] = {2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8}
A2[] = {2, 1, 8, 3}
Output: 
2 2 1 1 8 8 3 5 6 7 9
Explanation: Array elements of A1[] are
sorted according to A2[]. So 2 comes first
then 1 comes, then comes 8, then finally 3
comes, now we append remaining elements in
sorted order.
Example 2:

Input:
N = 11 
M = 4
A1[] = {2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8}
A2[] = {99, 22, 444, 56}
Output: 
1 1 2 2 3 5 6 7 8 8 9
Explanation: No A1[] elements are in A2[]
so we cannot sort A1[] according to A2[].
Hence we sort the elements in non-decreasing 
order.
Your Task:
You don't need to read input or print anything. Your task is to complete the function sortA1ByA2() which takes the array A1[ ], array A2[ ] and their respective size N and M as input parameters and returns the sorted array A1[ ] such that the relative positions of the elements in A1[ ] are same as the elements in A2[ ]. For the elements not present in A2[ ] but in A1[ ], it appends them at the last in increasing order. 

Expected Time Complexity: O(N * Log(N)).
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N, M ≤ 106
1 ≤ A1[i], A2[i] ≤ 106
"""

class Solution:
    def relativeSort(self, A1, N, A2, M):
        # Step 1: Count frequencies of each element in A1
        freq = {}
        for num in A1:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        # Step 2: Sort A1 according to A2
        result = []
        
        # Append elements as per A2 order
        for num in A2:
            if num in freq:
                result.extend([num] * freq[num])
                del freq[num]
        
        # Append remaining elements in A1 in sorted order
        remaining = sorted(freq.keys())
        for num in remaining:
            result.extend([num] * freq[num])
        
        return result

# Driver code
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        A1 = list(map(int, input().split()))
        A2 = list(map(int, input().split()))
        
        ob = Solution()
        result = ob.relativeSort(A1, n, A2, m)
        print(*result)
