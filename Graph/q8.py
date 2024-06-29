"""
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.


Example 1:

Input:



Output: 1
Explanation: 3 -> 3 is a cycle

Example 2:

Input:


Output: 0
Explanation: no cycle in the graph

Your task:
You dont need to read input or print anything. Your task is to complete the function isCyclic() which takes the integer V denoting the number of vertices and adjacency list adj as input parameters and returns a boolean value denoting if the given directed graph contains a cycle or not.
In the adjacency list adj, element adj[i][j] represents an edge from i to j.


Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)


Constraints:
1 ≤ V, E ≤ 105
"""

from typing import List

class Solution:
    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
        visited = [False] * V
        recStack = [False] * V
        
        def dfs(v):
            visited[v] = True
            recStack[v] = True
            
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif recStack[neighbor]:
                    return True
            
            recStack[v] = False
            return False
        
        for i in range(V):
            if not visited[i]:
                if dfs(i):
                    return True
        
        return False

# Driver Code
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
        
        ob = Solution()
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
