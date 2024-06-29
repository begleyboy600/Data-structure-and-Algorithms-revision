"""
Given head of a linked list and a number k, your task is to find the kth node from the end. If k is more than the number of nodes, then the output should be -1.
The following is internal representation of every test case (three inputs).
n :  Size of the linked list
k : Postion (from end) of the node to be found
value[] :  An array of values that represents values of nodes.

Examples

Input: n = 9, k = 2, value[] = {1,2,3,4,5,6,7,8,9}
Output: 8
Explanation: The given linked list is 1->2->3->4->5->6->7->8->9. The 2nd node from end is 8.  
Input: n = 4, k = 5, value[] = {10,5,100,5}
Output: -1
Explanation: The given linked list is 10->5->100->5. Since 'k' is more than the number of nodes, the output is -1.
Note:  Try to solve in a single traversal.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).

Constraints:
1 <= n <= 106
1 <= k <= 106
"""


import atexit
import io
import sys

def getKthFromLast(head, k):
    if not head or k <= 0:
        return -1
    
    fast = head 
    slow = head

    for _ in range(k):
        if fast is None:
            return -1
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    if slow:
        return slow.data
    else:
        return -1


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n, k = map(int, input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        print(getKthFromLast(a.head, k))