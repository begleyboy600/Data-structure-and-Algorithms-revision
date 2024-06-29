"""
Given a Binary Tree, find its Boundary Traversal. The traversal should be in the following order: 

Left boundary nodes: defined as the path from the root to the left-most node ie- the leaf node you could reach when you always travel preferring the left subtree over the right subtree. 
Leaf nodes: All the leaf nodes except for the ones that are part of left or right boundary.
Reverse right boundary nodes: defined as the path from the right-most node to the root. The right-most node is the leaf node you could reach when you always travel preferring the right subtree over the left subtree. Exclude the root from this as it was already included in the traversal of left boundary nodes.
Note: If the root doesn't have a left subtree or right subtree, then the root itself is the left or right boundary. 

Example 1:

Input:
        1 
      /   \
     2     3  
    / \   / \ 
   4   5 6   7
      / \
     8   9
   
Output: 1 2 4 8 9 6 7 3
Explanation:


 

Example 2:

Input:
            1
           /
          2
        /  \
       4    9
     /  \    \
    6    5    3
             /  \
            7     8

Output: 1 2 4 6 5 7 8
Explanation:















As you can see we have not taken the right subtree. 
Your Task:
This is a function problem. You don't have to take input. Just complete the function boundary() that takes the root node as input and returns an array containing the boundary values in anti-clockwise.

Expected Time Complexity: O(N). 
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 ≤ Number of nodes ≤ 105
1 ≤ Data of a node ≤ 105
"""

class Solution:
    def printBoundaryView(self, root):
        if not root:
            return []
        
        result = []

        # Function to collect left boundary excluding leaf nodes
        def leftBoundary(node):
            while node:
                if node.left or node.right:
                    result.append(node.data)
                if node.left:
                    node = node.left
                else:
                    node = node.right

        # Function to collect all leaf nodes
        def leafNodes(node):
            if node:
                leafNodes(node.left)
                if not node.left and not node.right:
                    result.append(node.data)
                leafNodes(node.right)

        # Function to collect right boundary excluding leaf nodes
        def rightBoundary(node):
            stack = []
            while node:
                if node.left or node.right:
                    stack.append(node.data)
                if node.right:
                    node = node.right
                else:
                    node = node.left
            while stack:
                result.append(stack.pop())

        # Include the root node
        result.append(root.data)

        # Get left boundary, leaf nodes, and right boundary
        leftBoundary(root.left)
        leafNodes(root)
        rightBoundary(root.right)
        
        return result

# { 
# Driver Code Starts
# Initial Template for Python 3

import sys
sys.setrecursionlimit(100000)

# Contributed by Sudarshan Sharma
from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == "N":           
        return None
        
    # Creating list of strings from input 
    # string after splitting by space
    ip = list(map(str, s.split()))
    
    # Create the root of the tree
    root = Node(int(ip[0]))                     
    size = 0
    q = deque()
    
    # Push the root to the queue
    q.append(root)                            
    size = size + 1 
    
    # Starting from the second element
    i = 1                                       
    while size > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1
        
        # Get the current node's value from the string
        currVal = ip[i]
        
        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if i >= len(ip):
            break
        currVal = ip[i]
        
        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)
        obj = Solution()
        res = obj.printBoundaryView(root)
        for i in res:
            print(i, end=" ")
        print('')
# } Driver Code Ends
