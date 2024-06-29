"""
Given two strings str1 & str 2 of length n & m respectively, return the length of their longest common subsequence. If there is no common subsequence then, return 0. 

A subsequence is a sequence that can be derived from the given string by deleting some or no elements without changing the order of the remaining elements. For example, "abe" is a subsequence of "abcde".

Example 1:

Input: n = 6, str1 = ABCDGH and m = 6, str2 = AEDFHR
Output: 3
Explanation: LCS for input strings “ABCDGH” and “AEDFHR” is “ADH” of length 3.
Example 2:

Input: n = 3, str1 = ABC and m = 2, str2 = AC
Output: 2
Explanation: LCS of "ABC" and "AC" is "AC" of length 2.
Example 3:

Input: n = 4, str1 = XYZW and m = 4, str2 = XYWZ
Output: 3
Explanation: There are two common subsequences of length 3 “XYZ”, and”XYW”, and no common subsequence. of length more than 3.
Your Task:
You do not need to read input or print anything. Complete the function lcs() which takes the two strings and their lengths as input parameters and returns the length of the Longest Common Subsequence. 

Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)

Constraints:
1<= n, m <=103
str1 and str2 are in uppercase alphabet
"""

class Solution:
    # Function to find the length of longest common subsequence in two strings.
    def lcs(self, n, m, str1, str2):
        # Create a 2D array to store the lengths of longest common subsequence.
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Building the dp array from the bottom up
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # The length of the longest common subsequence will be in dp[n][m]
        return dp[n][m]

# { 
# Driver Code Starts
# Initial Template for Python 3

import sys
input = sys.stdin.readline

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, m = map(int, input().strip().split())
        str1 = str(input()).strip()
        str2 = str(input()).strip()
        ob = Solution()
        print(ob.lcs(n, m, str1, str2))

# } Driver Code Ends
