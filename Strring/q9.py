"""
Explanation: It is constructed by 
appending "ab" 3 times
Example 2:

Input: s = "ababac"
Output: 0
Explanation: Not possible to construct
Your Task:
Your task is to complete the function isRepeat() which takes a single string as input and returns 1 if possible to construct, otherwise 0. You do not need to take any input or print anything.

Expected Time Complexity: O(|s|)
Expected Auxiliary Space: O(|s|)

Constraints:
1 <= |s| <= 105
"""

class Solution:
    def isRepeat(self, s):
        # Concatenate the string with itself and remove the first and last character
        doubled_s = (s + s)[1:-1]

        # Check if the original string exists in this new string
        if s in doubled_s:
            return 1
        else:
            return 0
        

# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input().strip()
        
        ob = Solution()
        answer = ob.isRepeat(s)
        
        print(answer)

# Driver Code Ends
