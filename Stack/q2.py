"""
Given a stack, the task is to sort it such that the top of the stack has the greatest element.

Example 1:

Input:
Stack: 3 2 1
Output: 3 2 1
Example 2:

Input:
Stack: 11 2 32 3 41
Output: 41 32 11 3 2
Your Task: 
You don't have to read input or print anything. Your task is to complete the function sort() which sorts the elements present in the given stack. (The sorted stack is printed by the driver's code by popping the elements of the stack.)

Expected Time Complexity: O(N*N)
Expected Auxilliary Space: O(N) recursive.

Constraints:
1<=N<=100
"""

class Solution:
    def sortStack(self, s):
        if len(s) <= 1:
            return
        
        top = s.pop()
        self.sortStack(s)
        self.insertInSortedOrder(s, top)
    
    def insertInSortedOrder(self, s, element):
        if len(s) == 0 or s[-1] <= element:
            s.append(element)
        else:
            top = s.pop()
            self.insertInSortedOrder(s, element)
            s.append(top)


if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sortStack(arr)
        while arr:
            print(arr.pop(), end=" ")
        print()
