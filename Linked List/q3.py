"""
Given the head of a singly linked list, the task is to check if the linked list has a loop. A loop means that the last node of the linked list is connected back to a node in the same list.  So if the next of the last node is null. then there is no loop. We need to return true if there is a loop, otherwise false.

The following is an internal representation of every test case (three inputs).
n : Size of the linked list
value[] :  An array of values that represents values of nodes.
pos (1 based index) :  Position of the node to which the last node links back if there is a loop. If the linked list does not have any loop, then pos = 0.

Examples:

Input: n = 3, value[] = {1,3,4}, pos = 2
Output: True
Explanation: 

See the above list there exists a loop connecting the last node back to the second node.
Input: n = 4, value[] = {1,8,3,4}, pos = 0
Output: False
Explanation: 

There is no loop exists.
Input: n = 4, value[] = {1,2,3,4}, pos = 1
Output: True
Explanation:

A loop is present connecting the last node back to the first node.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ n ≤ 104
1 ≤ value[i] ≤ 103
"""

class Solution:
    def detectLoop(self, head):
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next

        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return True


# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
    
    # connects last node to node at position pos from beginning.
    def loopHere(self, pos):
        if pos == 0:
            return
        
        walk = self.head
        for i in range(1, pos):
            walk = walk.next
        
        self.tail.next = walk

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        
        LL = LinkedList()
        values = list(map(int, input().split()))
        for val in values:
            LL.insert(val)
        
        pos = int(input())
        LL.loopHere(pos)
        
        print(Solution().detectLoop(LL.head))
# } Driver Code Ends