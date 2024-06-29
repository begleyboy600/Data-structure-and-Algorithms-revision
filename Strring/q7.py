"""
Given a string in roman no format (s)  your task is to convert it to an integer . Various symbols and their values are given below.
I 1
V 5
X 10
L 50
C 100
D 500
M 1000

Example 1:

Input:
s = V
Output: 5
Example 2:

Input:
s = III 
Output: 3
Your Task:
Complete the function romanToDecimal() which takes a string as input parameter and returns the equivalent decimal number. 

Expected Time Complexity: O(|S|), |S| = length of string S.
Expected Auxiliary Space: O(1)

Constraints:
1<=roman no range<=3999
"""

class Solution:
    def romanToDecimal(self, S):
        # Dictionary to map Roman numerals to their values
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        n = len(S)

        for i in range(n):
            # If this is not the last character and the current character's value is less than the next character's value
            if i + 1 < n and roman_values[S[i]] < roman_values[S[i + 1]]:
                total -= roman_values[S[i]]
            else:
                total += roman_values[S[i]]
        return total
    

# Driver Code Starts
# Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# Driver Code Ends