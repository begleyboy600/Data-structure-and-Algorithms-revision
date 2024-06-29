"""
Given a string S. The task is to find the first repeated character in it. We need to find the character that occurs more than once and whose index of second occurrence is smallest. S contains only lowercase letters.

 

Example 1:

Input: S="geeksforgeeks"
Output: e
Explanation: 'e' repeats at third position.
 

Example 2:

Input: S="hellogeeks"
Output: l
Explanation: 'l' repeats at fourth position.
 

Example 3:

Input: S="abc"
Output: -1
Explanation: There is no repeated character.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function firstRepChar() which accepts a string S as input parameter and returns a string containing first repeated character in it. If there is no repeated character in the string S then return "-1".
 

Expected Time Complexity: O(|S|) 
Expected Auxiliary Space: O(1)
where |S| denotes the length of string S
"""

class Solution:
    def firstRepChar(self, s: str) -> str:
        seen = set()
        first_repeated = None
        min_index = float('inf')
        
        for index, ch in enumerate(s):
            if ch in seen:
                if first_repeated is None or index < min_index:
                    first_repeated = ch
                    min_index = index
            else:
                seen.add(ch)
        
        if first_repeated:
            return first_repeated
        else:
            return "-1"

# Driver code
if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        sol = Solution()
        print(sol.firstRepChar(s))
