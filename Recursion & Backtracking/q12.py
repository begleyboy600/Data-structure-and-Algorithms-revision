"""
Given a number K and string str of digits denoting a positive integer, build the largest number possible by performing swap operations on the digits of str at most K times.


Example 1:

Input:
K = 4
str = "1234567"
Output:
7654321
Explanation:
Three swaps can make the
input 1234567 to 7654321, swapping 1
with 7, 2 with 6 and finally 3 with 5
Example 2:

Input:
K = 3
str = "3435335"
Output:
5543333
Explanation:
Three swaps can make the input
3435335 to 5543333, swapping 3 
with 5, 4 with 5 and finally 3 with 4 

Your task:
You don't have to read input or print anything. Your task is to complete the function findMaximumNum() which takes the string and an integer as input and returns a string containing the largest number formed by perfoming the swap operation at most k times.


Expected Time Complexity: O(n!/(n-k)!) , where n = length of input string
Expected Auxiliary Space: O(n)


Constraints:
1 ≤ |str| ≤ 30
1 ≤ K ≤ 10
"""

class Solution:
    
    def findMaximumNum(self, s, k):
        # Helper function for the backtracking
        def find_maximum(s, k, max_num, index):
            if k == 0 or index == len(s):
                return
            
            max_char = max(s[index:])
            if max_char != s[index]:
                k -= 1
            
            for i in range(index, len(s)):
                if s[i] == max_char:
                    # Swap characters
                    s = s[:index] + s[i] + s[index + 1:i] + s[index] + s[i + 1:]
                    if s > max_num[0]:
                        max_num[0] = s
                    
                    find_maximum(s, k, max_num, index + 1)
                    
                    # Swap back to restore original string
                    s = s[:index] + s[i] + s[index + 1:i] + s[index] + s[i + 1:]
        
        max_num = [s]
        find_maximum(s, k, max_num, 0)
        return max_num[0]


# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        k = int(input())
        s = input()
        ob = Solution()
        print(ob.findMaximumNum(s, k))

# Driver Code Ends

