"""
Given an integer n. Return the nth row of the following look-and-say pattern.
1
11
21
1211
111221
Look-and-Say Pattern:

To generate a member of the sequence from the previous member, read off the digits of the previous member, counting the number of digits in groups of the same digit. For example:

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
1211 is read off as "one 1, one 2, then two 1s" or 111221.
111221 is read off as "three 1s, two 2s, then one 1" or 312211.
Example 1:

Input:
n = 5
Output: 111221
Explanation: The 5th row of the given pattern
will be 111221.
Example 2:

Input:
n = 3
Output: 21
Explanation: The 3rd row of the given pattern
will be 21.

Your Task:  
You dont need to read input or print anything. Complete the function lookandsay() which takes integer n as input parameter and returns a string denoting the contents of the nth row of given pattern.


Expected Time Complexity: O(2n)
Expected Auxiliary Space: O(2n-1)  


Constraints:
1 ≤ n ≤ 30
"""

class Solution:
    def lookandsay(self, n):
        if n <= 0:
            return ""
        
        # base case 
        sequence = "1"

        for _ in range(2, n + 1):
            next_sequence = ""
            i = 0
            while i < len(sequence):
                count = 1
                while i + 1 < len(sequence) and sequence[i] == sequence[i + 1]:
                    count += 1
                    i += 1
                next_sequence += str(count) + sequence[i]
                i += 1
            sequence = next_sequence
        
        return sequence
    
# Driver code
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        solObj = Solution()
        print(solObj.lookandsay(n))