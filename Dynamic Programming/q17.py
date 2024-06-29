"""
Given a String, find the longest palindromic subsequence.

NOTE: Subsequence of a given sequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the order of the remaining elements

Example 1:

Input:
S = "bbabcbcab"
Output: 7
Explanation: Subsequence "babcbab" is the
longest subsequence which is also a palindrome.


Example 2:

Input: 
S = "abcd"
Output: 1
Explanation: "a", "b", "c" and "d" are
palindromic and all have a length 1.

Your Task:
You don't need to read input or print anything. Your task is to complete the function longestPalinSubseq() which takes the string S as input and returns an integer denoting the length of the longest palindromic subsequence of S.

Expected Time Complexity: O(|S|*|S|).
Expected Auxiliary Space: O(|S|*|S|).

Constraints:
1 ≤ |S| ≤ 1000
"""

class Solution:
    def longestPalinSubseq(self, S):
        n = len(S)
        if n == 0:
            return 0
        
        # Create a 2D dp array
        dp = [[0]*n for _ in range(n)]
        
        # All single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1
        
        # Build the dp table
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if S[i] == S[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        # The longest palindromic subsequence length for the whole string
        return dp[0][n - 1]

# Driver code
if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        obj = Solution()
        print(obj.longestPalinSubseq(s))
