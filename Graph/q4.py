"""
Given an adjacency list for a Directed Acyclic Graph (DAG) where adj_list[i] contains a list of all vertices j such that there is a directed edge from vertex i to vertex j, with  V  vertices and E  edges, your task is to find any valid topological sorting of the graph.

 

In a topological sort, for every directed edge u -> v,  u must come before v in the ordering.

 

Example 1:

Input:

Output:
1
Explanation:
The output 1 denotes that the order is
valid. So, if you have, implemented
your function correctly, then output
would be 1 for all test cases.
One possible Topological order for the
graph is 3, 2, 1, 0.
Example 2:

Input:

Output:
1
Explanation:
The output 1 denotes that the order is
valid. So, if you have, implemented
your function correctly, then output
would be 1 for all test cases.
One possible Topological order for the
graph is 5, 4, 2, 1, 3, 0.
Your Task:
You don't need to read input or print anything. Your task is to complete the function topoSort()  which takes the integer V denoting the number of vertices and adjacency list as input parameters and returns an array consisting of the vertices in Topological order. As there are multiple Topological orders possible, you may return any of them. If your returned topo sort is correct then the console output will be 1 else 0.

Expected Time Complexity: O(V + E).
Expected Auxiliary Space: O(V).

Constraints:
2 ≤ V ≤ 104
1 ≤ E ≤ (N*(N-1))/2
"""

from collections import deque

class Solution:
    def topoSort(self, V, adj):
        in_degree = [0] * V
        
        # Calculate in-degree for each vertex
        for vertex in range(V):
            for neighbor in adj[vertex]:
                in_degree[neighbor] += 1
        
        # Queue for vertices with zero in-degree
        zero_in_degree_queue = deque()
        for vertex in range(V):
            if in_degree[vertex] == 0:
                zero_in_degree_queue.append(vertex)
        
        topological_order = []
        
        while zero_in_degree_queue:
            vertex = zero_in_degree_queue.popleft()
            topological_order.append(vertex)
            
            for neighbor in adj[vertex]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    zero_in_degree_queue.append(neighbor)
        
        return topological_order

# Driver Code
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        e, N = map(int, input().strip().split())
        adj = [[] for _ in range(N)]
        
        for _ in range(e):
            u, v = map(int, input().split())
            adj[u].append(v)
        
        obj = Solution()
        res = obj.topoSort(N, adj)
        
        # Checking if the result is a valid topological order
        is_valid = True
        if len(res) != N:
            is_valid = False
        else:
            seen = [False] * N
            for vertex in res:
                if seen[vertex]:
                    is_valid = False
                    break
                seen[vertex] = True
                for neighbor in adj[vertex]:
                    if not seen[neighbor]:
                        is_valid = False
                        break
                if not is_valid:
                    break
        
        if is_valid:
            print(1)
        else:
            print(0)
