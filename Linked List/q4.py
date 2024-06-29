"""
Given head of a linked list that may contain a loop.  A loops means that the last node of the linked list is connected back to a node in the same list.  So if next of the last node is null. then there is no loop.  Remove loop from the linked list, if it is present (we mainly need to make next of the last node as null). Otherwise keep the linked list as it is.

The following is internal representation of every test case (three inputs).
n : Size of the linked list
value[] :  An array of values that represents values of nodes.
pos (1 based index) :  Position of the node to which the last node links back if there is a loop. If the linked list does not have any loop, then pos = 0.

The generated output will be 1 if your submitted code is correct.

Examples:

Input: n = 3, value[] = {1,3,4}, pos = 2
Output: 1
Explanation: The linked list looks like

A loop is present. If you remove it successfully, the answer will be 1. 
Input: n = 4, value[] = {1,8,3,4}, pos = 0
Output: 1
Explanation: 

The Linked list does not contains any loop. 
Input: n = 4, value[] = {1,2,3,4}, pos = 1
Output: 1
Explanation: The linked list looks like 

A loop is present. If you remove it successfully, the answer will be 1. 
Expected time complexity: O(n)
Expected auxiliary space: O(1)

Constraints:
1 ≤ n ≤ 10^4
"""

class Solution:
    def removeLoop(self, head):
        if not head or not head.next:
            return 
        
        # Function to detect and return the start node of the loop if present
        def detectAndFindLoopStart(head):
            slow = head 
            fast = head

            while fast and fast.next:
                slow = slow.next
                fast.next.next

                if slow == fast:
                    return slow
            return slow
        
        def removeTheLoop(loopStart, head):
            ptr1 = head
            ptr2 = loopStart

            while ptr1.next != ptr2.next:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            
            ptr2.next = None
        
        loopStart = detectAndFindLoopStart(head)

        if loopStart:
            removeTheLoop(loopStart, head)



class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,num):
        if self.head is None:
            self.head=Node(num)
            self.tail=self.head
        else:
            self.tail.next=Node(num)
            self.tail=self.tail.next
    
    def isLoop(self):
        if self.head is None:
            return False
        
        fast=self.head.next
        slow=self.head
        
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            fast=fast.next.next
            slow=slow.next
        
        return True
    
    def loopHere(self,position):
        if position==0:
            return
        
        walk=self.head
        for _ in range(1,position):
            walk=walk.next
        self.tail.next=walk
    
    def length(self):
        walk=self.head
        ret=0
        while walk:
            ret+=1
            walk=walk.next
        return ret

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=tuple(int(x) for x in input().split())
        pos=int(input())
        
        ll = linkedList()
        for i in arr:
            ll.add(i)
        ll.loopHere(pos)
        
        Solution().removeLoop(ll.head)
        
        if ll.isLoop() or ll.length()!=n:
            print(0)
            continue
        else:
            print(1)

