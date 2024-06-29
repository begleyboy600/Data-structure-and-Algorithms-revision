"""
Given a string, s, the objective is to convert it into integer format without utilizing any built-in functions. If the conversion is not feasible, the function should return -1.

Note: Conversion is feasible only if all characters in the string are numeric or if its first character is '-' and rest are numeric.

Example 1:

Input:
s = "-123"
Output: 
-123
Explanation:
It is possible to convert -123 into an integer 
and is so returned in the form of an integer
Example 2:

Input:
s = "21a"
Output: 
-1
Explanation: 
The output is -1 as, due to the inclusion of 'a',
the given string cannot be converted to an integer.
Your Task:
You do not have to take any input or print anything. Complete the function atoi() which takes a string s as an input parameter and returns an integer value representing the given string. If the conversion is not feasible, the function should return -1.

|s| = length of string str.
Expected Time Complexity: O( |s| ), 
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ |s| ≤ 10
"""

class Solution:
    def atoi(self, s):
        # Check if the string is empty
        if not s:
            return -1
        
        # Check if the string starts with a negative sign
        is_negative = False
        if s[0] == '-':
            is_negative = True
            s = s[1:]

        # If the string is empty after removing the negative sign, return -1
        if not s:
            return -1
        
        result = 0

        for char in s:
            if char < '0' or char > '9':
                return -1 

            result = result * 10 + (ord(char) - ord('0'))

        if is_negative:
            result = -result
        
        return result
    
# Driver Code Starts
# Initial template for Python

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        string = input().strip()
        ob = Solution()
        print(ob.atoi(string))
# } Driver Code Ends