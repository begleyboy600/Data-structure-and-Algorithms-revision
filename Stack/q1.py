"""
Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']', verify the validity of the arrangement.
An input string is valid if:

         1. Open brackets must be closed by the same type of brackets.
         2. Open brackets must be closed in the correct order.

Example 1:

Input:
S = ()[]{}
Output: 1
Explanation: The arrangement is valid, as both the conditions are followed here.
Example 2:

Input:
S = ())({}
Output: 0
Explanation: Arrangement is not valid, as for the bold closing bracket in ())({}, there is no opening bracket of similar kind, before it.
Your Task:  
You dont need to read input or print anything. Complete the function valid() which takes s as input and returns a boolean value denoting whether the arrangement is valid or not.

Expected Time Complexity: O(N) where N is the length of s.
Expected Auxiliary Space: O(N) 

Constraints:
1 <= N <= 105
"""

class Solution:
    def valid(self, s: str) -> bool:
        stack = []
        matching_bracket = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack:
                    return False
                top = stack.pop()
                if matching_bracket[char] != top:
                    return False
        
        return len(stack) == 0


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        if ob.valid(s):
            print(1)
        else:
            print(0)
# } Driver Code Ends