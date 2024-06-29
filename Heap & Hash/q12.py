"""
Given a string 's'. The task is to find the smallest window length that contains all the characters of the given string at least one time.
For eg. A = aabcbcdbca, then the result would be 4 as of the smallest window will be dbca.

 

Example 1:

Input : "AABBBCBBAC"
Output : 3
Explanation : Sub-string -> "BAC"
Example 2:
Input : "aaab"
Output : 2
Explanation : Sub-string -> "ab"
 
Example 3:
Input : "GEEKSGEEKSFOR"
Output : 8
Explanation : Sub-string -> "GEEKSFOR"
 


Your Task:  
You don't need to read input or print anything. Your task is to complete the function findSubString() which takes the string  S as input and returns the length of the smallest such window of the string.


Expected Time Complexity: O(256.N)
Expected Auxiliary Space: O(256)

 

Constraints:
1 ≤ |S| ≤ 105
String may contain both type of English Alphabets.
"""

class Solution:
    def findSubString(self, s: str) -> int:
        from collections import defaultdict
        
        if not s:
            return 0
        
        required = len(set(s))
        freq = defaultdict(int)
        formed = 0
        left = 0
        min_length = float('inf')
        
        for right in range(len(s)):
            freq[s[right]] += 1
            if freq[s[right]] == 1:
                formed += 1
            
            while formed == required:
                current_length = right - left + 1
                if current_length < min_length:
                    min_length = current_length
                
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    formed -= 1
                left += 1
        
        return min_length

# Driver code
def main():
    T = int(input().strip())
    for _ in range(T):
        s = input().strip()
        sol = Solution()
        print(sol.findSubString(s))

if __name__ == "__main__":
    main()
