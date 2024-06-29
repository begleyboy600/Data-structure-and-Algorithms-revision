"""
Given a string s and a dictionary of n words dictionary, find out if "s" can be segmented into a space-separated sequence of dictionary words.
Return 1 if it is possible to break the s into a sequence of dictionary words, else return 0. 

Note: From the dictionary dictionary each word can be taken any number of times and in any order.

Examples :

Input: n = 6, s = "ilike", dictionary = { "i", "like", "sam", "sung", "samsung", "mobile"}
Output: 1
Explanation: The string can be segmented as "i like".
Input: n = 6, s = "ilikesamsung", dictionary = { "i", "like", "sam", "sung", "samsung", "mobile"}
Output: 1
Explanation: The string can be segmented as "i like samsung" or "i like sam sung".
Expected Time Complexity: O(len(s)2)
Expected Space Complexity: O(len(s))

Constraints:
1 ≤ n ≤ 12
1 ≤ len(s) ≤ 1100
"""

class Solution:
    def wordBreak(self, n, s, dictionary):
        # Create a set for faster lookup
        word_set = set(dictionary)
        # Length of the string
        len_s = len(s)
        # Initialize dp array
        dp = [False] * (len_s + 1)
        dp[0] = True  # Empty string is always breakable
        
        for i in range(1, len_s + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[len_s]

# Driver code
if __name__ == '__main__':
    test_case = int(input())
    for _ in range(test_case):
        n = int(input())
        dictionary = input().strip().split()
        s = input().strip()
        ob = Solution()
        res = ob.wordBreak(n, s, dictionary)
        if res:
            print(1)
        else:
            print(0)
