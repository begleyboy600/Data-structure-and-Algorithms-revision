"""
Given two strings 'str' and a wildcard pattern 'pattern' of length N and M respectively, You have to return '1' if the wildcard pattern is matched with str else return '0' . All characters of the string str and pattern always belong to the Alphanumeric characters.


The wildcard pattern can include the characters ‘?’ and ‘*’
‘?’ – matches any single character.
‘*’ – Matches any sequence of characters (including the empty sequence).

Note: The matching should cover the entire str (not partial str).

 

Example 1:

Input:
pattern = "ba*a?"
str = "baaabab"
Output: 1
Explanation: replace '*' with "aab" and 
'?' with 'b'. 
Example 2:

Input:
pattern = "a*ab"
str = "baaabab"
Output: 0
Explanation: Because in string pattern character 'a' at first position,
pattern and str can't be matched. 

Your Task:
You don't need to read input or print anything. Your task is to complete the function wildCard() which takes the two strings 'pattern' and 'str' as input parameters and returns the answer.

 

Expected Time Complexity: O(N*M)
Expected Auxiliary Space: O(N*M)

Constraints:
1 <= length of(str, pattern) <= 200
"""

class Solution:
    def wildCard(self, pattern, string):
        N = len(pattern)
        M = len(string)
        
        # Initialize dp table with False
        dp = [[False] * (M + 1) for _ in range(N + 1)]
        
        # Empty pattern matches empty string
        dp[0][0] = True
        
        # Initialize first row
        for j in range(1, M + 1):
            dp[0][j] = False
        
        # Initialize first column
        for i in range(1, N + 1):
            if pattern[i - 1] == '*':
                dp[i][0] = dp[i - 1][0]
        
        # Fill the dp table
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if pattern[i - 1] == '?' or pattern[i - 1] == string[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif pattern[i - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = False
        
        return dp[N][M]

# Driver code
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        pattern = input().strip()
        string = input().strip()
        if Solution().wildCard(pattern, string):
            print(1)
        else:
            print(0)
