"""
Given a non-negative integer n. Reverse the bits of n and print the number obtained after reversing the bits.
Note:  The actual binary representation of the number is being considered for reversing the bits, no leading 0’s are being considered.
 
Example 1:
Input : 
N = 11
Output:
13
Explanation:
(11)10 = (1011)2.
After reversing the bits we get:
(1101)2 = (13)10.
Example 2:

Input : 
N = 10
Output:
5
Explanation:
(10)10 = (1010)2.
After reversing the bits we get:
(0101)2 = (101)2
        = (5)10.
Your task:
You don't need to read input or print anything. Your task is to complete the function reverseBits() which takes an integer N as input and returns the number obtained after reversing bits.
 
Expected Time Complexity : O(number of bits in the binary representation of N)
Expected Auxiliary Space :  O(1)
 
Constraints :
1 ≤ N ≤ 109
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        # Number of bits to consider depends on the integer size, which is platform-dependent
        # For the constraints given (1 ≤ N ≤ 10^9), it will be within 30 bits
        num_bits = 32  # considering up to 32-bit integer, which is sufficient for N ≤ 10^9
        
        for _ in range(num_bits):
            result = result << 1  # left shift result by 1 to make space for the next bit
            result |= n & 1       # set the least significant bit of result based on n's LSB
            n = n >> 1            # right shift n to consider the next bit
        
        return result

# Driver code
def main():
    T = int(input().strip())  # number of test cases
    for _ in range(T):
        n = int(input().strip())  # read the integer n
        sol = Solution()
        print(sol.reverseBits(n))

if __name__ == "__main__":
    main()
