"""
Given a Binary Tree, return Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function leftView(), which accepts root of the tree as argument. If no left view is possible, return an empty tree.

Left view of following tree is 1 2 4 8.

          1
       /     \
     2        3
   /     \    /    \
  4     5   6    7
   \
     8   

Example 1:

Input:
   1
 /  \
3    2
Output: 1 3

Example 2:

Input:

Output: 10 20 40
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
0 <= Number of nodes <= 100
0 <= Data of a node <= 1000
"""

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        # Number of nodes at current level
        level_length = len(queue)
        
        for i in range(level_length):
            node = queue.popleft()
            
            # If this is the first node of this level
            if i == 0:
                result.append(node.data)
                
            # Add left node to queue if it exists
            if node.left:
                queue.append(node.left)
                
            # Add right node to queue if it exists
            if node.right:
                queue.append(node.right)
                
    return result

#{ 
 # Driver Code Starts
# Contributed by Sudarshan Sharma
from collections import deque

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
        result = LeftView(root)
        for value in result:
            print(value, end=" ")
        print()

# } Driver Code Ends
