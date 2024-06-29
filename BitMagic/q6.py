"""
Given two integers A and B, the task is to find an integer X such that (X XOR A) is minimum possible and the count of set bit in X is equal to the count of set bits in B.

Example 1:

Input: 
A = 3, B = 5
Output: 3
Explanation:
Binary(A) = Binary(3) = 011
Binary(B) = Binary(5) = 101
The XOR will be minimum when x = 3
i.e. (3 XOR 3) = 0 and the number
of set bits in 3 is equal
to the number of set bits in 5.
Example 2:

Input: 
A = 7, B = 12
Output: 6
Explanation:
(7)2= 111
(12)2= 1100
The XOR will be minimum when x = 6 
i.e. (6 XOR 7) = 1 and the number 
of set bits in 6 is equal to the 
number of set bits in 12.
Your task :
You don't need to read input or print anything. Your task is to complete the function minVal() that takes integer A and B as input and returns the value of X according to the question.
 
Expected Time Complexity : O(log MAX(A,B))
Expected Auxiliary Space : O(1)
 
Constraints :
1 <= A, B <= 109
"""

class Solution:
    def minVal(self, A, B):
        # Count the number of set bits in B
        k = bin(B).count('1')
        
        # Start with X = 0
        X = 0
        
        # We'll iterate through each bit of B to set corresponding bits in X
        bit_position = 0
        while B > 0:
            if B & 1:  # Check if the current bit in B is set
                if not (A & (1 << bit_position)):  # Check if the corresponding bit in A is 0
                    X |= (1 << bit_position)  # Set the corresponding bit in X
            B >>= 1  # Move to the next bit in B
            bit_position += 1
        
        return X

# Driver code
if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        A = int(input().strip())
        B = int(input().strip())
        obj = Solution()
        print(obj.minVal(A, B))
