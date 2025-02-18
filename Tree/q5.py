"""
Given a Binary Tree, find Right view of it. Right view of a Binary Tree is set of nodes visible when tree is viewed from right side.

Right view of following tree is 1 3 7 8.

          1
       /     \
     2        3
   /   \      /    \
  4     5   6    7
    \
     8

Example 1:

Input:
       1
    /    \
   3      2
Output: 1 2
Example 2:

Input:
     10
    /   \
  20     30
 /   \
40  60 
Output: 10 30 60
Your Task:
Just complete the function rightView() that takes node as parameter and returns the right view as a list. 

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 ≤ Number of nodes ≤ 105
0 ≤ Data of a node ≤ 105
"""

# Node Class:
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to return list containing elements of right view of binary tree.
    def rightView(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                
                # If this is the last node of this level
                if i == level_length - 1:
                    result.append(node.data)
                    
                # Add right node to queue if it exists
                if node.right:
                    queue.append(node.right)
                
                # Add left node to queue if it exists
                if node.left:
                    queue.append(node.left)
                    
        return result


# { 
#  Driver Code Starts
# Initial Template for Python 3

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
    size += 1
    
    # Starting from the second element
    i = 1
    while size > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size -= 1
        
        # Get the current node's value from the string
        currVal = ip[i]
        
        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.left)
            size += 1
        
        # For the right child
        i += 1
        if i >= len(ip):
            break
        currVal = ip[i]
        
        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.right)
            size += 1
        i += 1
    return root

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)
        result = Solution().rightView(root)
        for value in result:
            print(value, end = " ")
        print()

# } Driver Code Ends
