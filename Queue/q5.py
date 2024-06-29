"""
Given a Queue Q containing N elements. The task is to reverse the Queue. Your task is to complete the function rev(), that reverses the N elements of the queue.

Example 1:

Input:
6
4 3 1 10 2 6
Output: 
6 2 10 1 3 4
Explanation: 
After reversing the given elements of the queue , the resultant queue will be 6 2 10 1 3 4.
Example 2:

Input:
4
4 3 2 1 
Output: 
1 2 3 4
Explanation: 
After reversing the given elements of the queue , the resultant queue will be 1 2 3 4.
Your Task: You need to complete the function rev that takes a queue as parameter and returns the reversed queue. The printing is done automatically by the driver code.

Expected Time Complexity : O(n)
Expected Auxilliary Space : O(n)

Constraints:
1 ≤ N ≤ 105
1 ≤ elements of Queue ≤ 105
"""

from queue import Queue

class Solution:
    # Function to reverse the queue.
    def rev(self, q):
        stack = []
        
        # Dequeue all elements into stack
        while not q.empty():
            stack.append(q.get())
        
        # Enqueue elements from stack into queue (now in reversed order)
        while stack:
            q.put(stack.pop())
        
        return q

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        q = Queue(maxsize=n)
        
        for num in a:
            q.put(num)
        
        ob = Solution()
        q = ob.rev(q)
        
        while not q.empty():
            print(q.get(), end=" ")
        print()

if __name__ == '__main__':
    main()
