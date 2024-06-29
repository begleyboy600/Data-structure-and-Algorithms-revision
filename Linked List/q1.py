"""
Given head a linked list, the task is to reverse this list.

The following is internal representation of every test case (two inputs).
n : Size of the linked list
value[] :  An array of values that represents values of nodes.

Examples:

Input: n = 6, value[] = {1, 2, 3, 4, 5, 6}
Output: 6 5 4 3 2 1
Explanation:

Input: n = 5, value[] = {2, 7, 10, 9, 8} 
Output: 8 9 10 7 2
Explanation:

Input: n = 1, value[] = {10}
Output: 10
Explanation: For a single node list, the reverse would be same as original
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).

Constraints:
1 <= n <= 104
"""

# Node Class
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

class Solution:
    def reverseList(self, head):
        prev = None 
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current 
            current = next_node
        
        return prev

# Function to print the linked list
def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp = tmp.next
    print()

# Driver Code
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        
        lis = Linked_List()
        for i in arr:
            lis.insert(i)
        
        sol = Solution()
        newHead = sol.reverseList(lis.head)
        printList(newHead)