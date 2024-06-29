"""
Explanation: The two people at the party both
know each other. None of them is a celebrity.

Your Task:
You don't need to read input or print anything. Complete the function celebrity() which takes the matrix M and its size N as input parameters and returns the index of the celebrity. If no such celebrity is present, return -1.


Expected Time Complexity: O(N^2)
Expected Auxiliary Space: O(1)


Constraints:
1 <= N <= 3000
0 <= M[][] <= 1
"""
class Solution:
    def celebrity(self, M, n):
        left, right = 0, n - 1
        
        # Step 1: Find potential celebrity
        while left < right:
            if M[left][right] == 1:
                left += 1
            else:
                right -= 1
        
        # Step 2: Verify the candidate
        potential_celebrity = left
        
        # Check if potential_celebrity meets the criteria of being a celebrity
        for i in range(n):
            if i != potential_celebrity:
                if M[potential_celebrity][i] == 1 or M[i][potential_celebrity] == 0:
                    return -1
        
        return potential_celebrity if self.is_celebrity(M, n, potential_celebrity) else -1
    
    def is_celebrity(self, M, n, celeb):
        for i in range(n):
            if i != celeb:
                if M[celeb][i] == 1 or M[i][celeb] == 0:
                    return False
        return True


if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends