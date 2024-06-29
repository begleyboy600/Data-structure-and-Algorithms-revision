"""
Given two strings S and P. Find the smallest window in the string S consisting of all the characters(including duplicates) of the string P.  Return "-1" in case there is no such window present. In case there are multiple such windows of same length, return the one with the least starting index.
Note : All characters are in Lowercase alphabets. 

Example 1:

Input:
S = "timetopractice"
P = "toc"
Output: 
toprac
Explanation: "toprac" is the smallest
substring in which "toc" can be found.
Example 2:

Input:
S = "zoomlazapzo"
P = "oza"
Output: 
apzo
Explanation: "apzo" is the smallest 
substring in which "oza" can be found.
Your Task:
You don't need to read input or print anything. Your task is to complete the function smallestWindow() which takes two string S and P as input paramters and returns the smallest window in string S having all the characters of the string P. In case there are multiple such windows of same length, return the one with the least starting index. 

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(n) n = len(p)

 

Constraints: 
1 ≤ |S|, |P| ≤ 105
"""

class Solution:
    def smallestWindow(self, S, P):
        from collections import defaultdict

        lenS = len(S)
        lenP = len(P)

        if lenS < lenP:
            return "-1"
        
        # Frequency counters
        freqP = defaultdict(int)
        freqWindow = defaultdict(int)

        # Populate frequency of characters in P
        for char in P: 
            freqP[char] += 1
        
        # Sliding window variables
        min_len = float('inf')
        start_idx = 0
        left = 0
        count = 0

        # Traverse S with right pointer
        for right in range(lenS):
            # Include character at right pointer in window
            if S[right] in freqP:
                freqWindow[S[right]] += 1
                if freqWindow[S[right]] <= freqP[S[right]]:
                    count += 1

            # If window includes all characters of P
            while count == lenP:
                # Update minimum length and start index of window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start_idx = left

                # Try to shrink the window from left
                if S[left] in freqP:
                    freqWindow[S[left]] -= 1
                    if freqWindow[S[left]] < freqP[S[left]]:
                        count -= 1
                left += 1
        
        if min_len == float('inf'):
            return "-1"
        
        return S[start_idx:start_idx + min_len]
    

# Driver code
if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        S = input().strip()
        P = input().strip()
        sol = Solution()
        print(sol.smallestWindow(S, P))

