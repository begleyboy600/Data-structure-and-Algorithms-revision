"""
There are given N ropes of different lengths, we need to connect these ropes into one rope. The cost to connect two ropes is equal to sum of their lengths.
The task is to connect the ropes with minimum cost. Given N size array arr[] contains the lengths of the ropes. 

Example 1:

Input:
n = 4
arr[] = {4, 3, 2, 6}
Output: 
29
Explanation:
We can connect the ropes in following ways.
1) First connect ropes of lengths 2 and 3.
Which makes the array {4, 5, 6}. Cost of
this operation 2+3 = 5. 
2) Now connect ropes of lengths 4 and 5.
Which makes the array {9, 6}. Cost of
this operation 4+5 = 9.
3) Finally connect the two ropes and all
ropes have connected. Cost of this 
operation 9+6 =15
Total cost for connecting all ropes is 5
+ 9 + 15 = 29. This is the optimized cost
for connecting ropes. 
Other ways of connecting ropes would always 
have same or more cost. For example, if we 
connect 4 and 6 first (we get three rope of 3,
2 and 10), then connect 10 and 3 (we get
two rope of 13 and 2). Finally we
connect 13 and 2. Total cost in this way
is 10 + 13 + 15 = 38.
Example 2:

Input:
n = 5
arr[] = {4, 2, 7, 6, 9}
Output: 
62 
Explanation:
First, connect ropes 4 and 2, which makes
the array {6,7,6,9}. Cost of
this operation 4+2 = 6. Next, add ropes 
6 and 6, which results in {12,7,9}. 
Cost of this operation 6+6 = 12.
Then, add 7 and 9, which makes the array {12,16}. 
Cost of this operation 7+9 = 16. And
finally, add these two which gives {28}.
Hence, the total cost is 6 + 12 + 16 + 
28 = 62.
Your Task:
You don't need to read input or print anything. Your task is to complete the function minCost() which takes an integer array arr[] and an integer n as arguments and returns the minimum cost.

Expected Time Complexity : O(nlogn)
Expected Auxilliary Space : O(n)

Constraints:
1 ≤ N ≤ 200000
1 ≤ arr[i] ≤ 106
"""

import heapq

class Solution:
    # Function to return the minimum cost of connecting the ropes.
    def minCost(self, arr, n):
        if n == 1:
            return 0
        
        # Initialize min-heap
        heapq.heapify(arr)
        
        min_cost = 0
        
        # Keep merging until only one rope left
        while len(arr) > 1:
            # Extract the two smallest ropes
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)
            
            # Cost to merge them
            current_cost = first + second
            min_cost += current_cost
            
            # Push the merged rope length back to the heap
            heapq.heappush(arr, current_cost)
        
        return min_cost

# Driver Code
if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()
    
    test_cases = int(data[0])
    index = 1
    for _ in range(test_cases):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        
        # Create an object of Solution class
        sol = Solution()
        # Compute and print the minimum cost
        print(sol.minCost(arr, n))
