"""
Given two numbers as strings s1 and s2. Calculate their Product.

Note: The numbers can be negative and You are not allowed to use any built-in function or convert the strings to integers. There can be zeros in the begining of the numbers. You don't need to specify '+' sign in the begining of positive numbers.

Example 1:

Input:
s1 = "0033"
s2 = "2"
Output:
66
Example 2:

Input:
s1 = "11"
s2 = "23"
Output:
253
Your Task: You don't need to read input or print anything. Your task is to complete the function multiplyStrings() which takes two strings s1 and s2 as input and returns their product as a string.

Expected Time Complexity: O(n1* n2)
Expected Auxiliary Space: O(n1 + n2); where n1 and n2 are sizes of strings s1 and s2 respectively.

Constraints:
1 ≤ length of s1 and s2 ≤ 103
"""

class Solution:
    def multiplyStrings(self, s1, s2):
        # Determine if the result should be negative
        negative = (s1[0] == '-') ^ (s2[0] == '-')
        
        # Remove any leading zeros and signs
        s1 = s1.lstrip('0').lstrip('-')
        s2 = s2.lstrip('0').lstrip('-')

        # Handle cases where the numbers might be zero
        if not s1 or not s2:
            return "0"

        # Initialize result array
        n1 = len(s1)
        n2 = len(s2)
        result = [0] * (n1 + n2)

        # Multiply each digit and add to result
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                mul = (ord(s1[i]) - ord('0')) * (ord(s2[j]) - ord('0'))
                sum = mul + result[i + j + 1]
                result[i + j + 1] = sum % 10
                result[i + j] += sum // 10

        # Convert result array to string, skipping leading zeros
        result_str = ''.join(map(str, result)).lstrip('0')

        # Add the negative sign if needed
        if negative and result_str != "0":
            result_str = '-' + result_str

        return result_str if result_str else "0"
    


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a, b = input().split()
        print(Solution().multiplyStrings(a.strip(), b.strip()))
