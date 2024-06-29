"""
Given an input stream of N integers. The task is to insert these numbers into a new stream and find the median of the stream formed by each insertion of X to the new stream.

Example 1:

Input:
N = 4
X[] = 5,15,1,3
Output:
5
10
5
4
Explanation:Flow in stream : 5, 15, 1, 3 
5 goes to stream --> median 5 (5) 
15 goes to stream --> median 10 (5,15) 
1 goes to stream --> median 5 (5,15,1) 
3 goes to stream --> median 4 (5,15,1 3) 
 

Example 2:

Input:
N = 3
X[] = 5,10,15
Output:
5
7.5
10
Explanation:Flow in stream : 5, 10, 15
5 goes to stream --> median 5 (5) 
10 goes to stream --> median 7.5 (5,10) 
15 goes to stream --> median 10 (5,10,15) 
Your Task:
You are required to complete the class Solution. 
It should have 2 data members to represent 2 heaps. 
It should have the following member functions:
insertHeap() which takes x as input and inserts it into the heap, the function should then call balanceHeaps() to balance the new heap.
balanceHeaps() does not take any arguments. It is supposed to balance the two heaps.
getMedian() does not take any arguments. It should return the current median of the stream.

Expected Time Complexity : O(nlogn)
Expected Auxilliary Space : O(n)
 
Constraints:
1 <= N <= 106
1 <= x <= 106
"""

import heapq
import atexit
import io
import sys
import heapq
from collections import  defaultdict
import math

class Solution:
    def __init__(self):
        self.left_max_heap = []    # Max-heap (invert values) for smaller half
        self.right_min_heap = []   # Min-heap for larger half
        
    def balanceHeaps(self):
        # Ensure the size of left_max_heap is not more than 1 greater than right_min_heap
        if len(self.left_max_heap) > len(self.right_min_heap) + 1:
            heapq.heappush(self.right_min_heap, -heapq.heappop(self.left_max_heap))
        elif len(self.right_min_heap) > len(self.left_max_heap):
            heapq.heappush(self.left_max_heap, -heapq.heappop(self.right_min_heap))
    
    def getMedian(self):
        if len(self.left_max_heap) == len(self.right_min_heap):
            return (self.left_max_heap[0] - self.right_min_heap[0]) / 2
        else:
            return -self.left_max_heap[0]
        
    def insertHeaps(self, x):
        if len(self.left_max_heap) == 0 or x <= -self.left_max_heap[0]:
            heapq.heappush(self.left_max_heap, -x)
        else:
            heapq.heappush(self.right_min_heap, x)
        
        self.balanceHeaps()

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ob=Solution()
        for i in range(n):
            x=int(input())
            ob.insertHeaps(x)
            print(math.floor(ob.getMedian()))

# } Driver Code Ends