"""
A Hamiltonian path, is a path in an undirected graph that visits each vertex exactly once. Given an undirected graph, the task is to check if a Hamiltonian path is present in it or not.

Example 1:

Input:
N = 4, M = 4
Edges[][]= { {1,2}, {2,3}, {3,4}, {2,4} }
Output:
1 
Explanation: 
There is a hamiltonian path: 
1 -> 2 -> 3 -> 4 
Example 2:

Input:
N = 4, M = 3 
Edges[][] = { {1,2}, {2,3}, {2,4} } 
Output: 
0 
Explanation: 
It can be proved that there is no 
hamiltonian path in the given graph
Your task:
You don't need to read input or print anything. Your task is to complete the function check() which takes the N (the number of vertices), M (Number of edges) and the list of Edges[][] (where Edges[i] denotes the undirected Edge between vertices Edge[i][0] and Edges[i][1] ) as input parameter and returns true (boolean value) if the graph contains Hamiltonian path,otherwise returns false. 


Expected Time Complexity: O(N!).
Expected Auxiliary Space: O(N+M).


Constraints:
1 ≤ N ≤ 10
1 ≤ M ≤ 15
Size of Edges[i] is 2
1 ≤ Edges[i][0],Edges[i][1] ≤ N
"""

from itertools import permutations

class Solution:
    def check(self, N, M, Edges):
        # Build adjacency list representation of the graph
        graph = [[] for _ in range(N + 1)]
        for u, v in Edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Function to check if a path is Hamiltonian
        def is_hamiltonian(path):
            visited = [False] * (N + 1)
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                if v not in graph[u] or visited[v]:
                    return False
                visited[v] = True
            return True
        
        # Check all permutations of vertices to find a Hamiltonian path
        vertices = list(range(1, N + 1))
        for perm in permutations(vertices):
            if is_hamiltonian(perm):
                return True
        
        return False

# Driver code
if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        N, M = map(int, input().strip().split())
        Edges = []
        e = list(map(int, input().strip().split()))
        for i in range(M):
            Edges.append([e[2*i], e[2*i+1]])
        
        ob = Solution()
        if ob.check(N, M, Edges):
            print(1)
        else:
            print(0)
