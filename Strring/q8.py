"""
Given a string S, find the length of the longest substring without repeating characters.


Example 1:

Input:
S = "geeksforgeeks"
Output:
7
Explanation:
Longest substring is
"eksforg".
Example 2:

Input:
S = "abdefgabef"
Output:
6
Explanation:
Longest substring are
"abdefg" , "bdefga" and "defgab".
 

Your Task:
You don't need to take input or print anything. Your task is to complete the function longestUniqueSubsttr() which takes a string S as and returns the length of the longest substring.

 

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(K) where K is constant.


Constraints:
1 ≤ |S| ≤ 105
It is guaranteed that all characters of the String S will be lowercase letters from 'a' to 'z'

"""

class Solution: 
    def longestUniqueSubsttr(self, S):
        last_seen = {}
        max_length = 0
        start = 0

        for i in range(len(S)):
            # If we have seen the character and it's within the current window
            if S[i] in last_seen and last_seen[S[i]] >= start:
                # Move the start to one position right to the last occurrence
                start = last_seen[S[i]] + 1
            
            # Update the last seen index of the character
            last_seen[S[i]] = i

            # Update the maximum length of substring found so far
            max_length = max(max_length, i - start + 1)

        return max_length

# Driver Code Starts
# Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        print(ob.longestUniqueSubsttr(s))
# Driver Code Ends
