"""
Given two strings s and t. Return the minimum number of operations required to convert s to t.
The possible operations are permitted:

Insert a character at any position of the string.
Remove any character from the string.
Replace any character from the string with any other character.
 

Example 1:

Input: 
s = "geek", t = "gesek"
Output: 1
Explanation: One operation is required 
inserting 's' between two 'e's of s.
Example 2:

Input : 
s = "gfg", t = "gfg"
Output: 
0
Explanation: Both strings are same.
 

Your Task:
You don't need to read or print anything. Your task is to complete the function editDistance() which takes strings s and t as input parameters and returns the minimum number of operation to convert the string s to string t. 


Expected Time Complexity: O(|s|*|t|)
Expected Space Complexity: O(|s|*|t|)


Constraints:
1 ≤ Length of both strings ≤ 100
Both the strings are in lowercase.
"""

class Solution:
    def editDistance(self, s, t):
        m, n = len(s), len(t)
        
        # Initialize DP table with zeros
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the DP table based on the conditions
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j  # All characters of t need to be inserted
                elif j == 0:
                    dp[i][j] = i  # All characters of s need to be deleted
                elif s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # No operation needed
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1],    # Insert
                                       dp[i - 1][j],    # Remove
                                       dp[i - 1][j - 1] # Replace
                                      )
        
        return dp[m][n]

# Driver Code
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        s, t = input().split()
        ob = Solution()
        ans = ob.editDistance(s, t)
        print(ans)
