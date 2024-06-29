"""
Given a number N. Find the length of the longest consecutive 1s in its binary representation.

Example 1:

Input: N = 14
Output: 3
Explanation: 
Binary representation of 14 is 
1110, in which 111 is the longest 
consecutive set bits of length is 3.
Example 2:

Input: N = 222
Output: 4
Explanation: 
Binary representation of 222 is 
11011110, in which 1111 is the 
longest consecutive set bits of length 4. 

Your Task: 
You don't need to read input or print anything. Your task is to complete the function maxConsecutiveOnes() which returns the length of the longest consecutive 1s in the binary representation of given N.

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 106
"""

class Solution:
    def maxConsecutiveOnes(self, N):
        # Initialize variables
        max_len = 0
        current_len = 0
        
        # Convert N to binary string and iterate over each character
        bin_rep = bin(N)[2:]  # binary representation of N, omitting '0b' prefix
        for bit in bin_rep:
            if bit == '1':
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                max_len = max(max_len, current_len)
                current_len = 0
        
        return max_len

# Driver code
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        obj = Solution()
        print(obj.maxConsecutiveOnes(n))
