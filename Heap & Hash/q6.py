"""
Given a string S with repeated characters. The task is to rearrange characters in a string such that no two adjacent characters are the same.
Note: The string has only lowercase English alphabets and it can have multiple solutions. Return any one of them.

Example 1:

Input : str = "geeksforgeeks"
Output: 1
Explanation: All the repeated characters of the
given string can be rearranged so that no 
adjacent characters in the string is equal.
Any correct rearrangement will show a output
of 1.
Example 2:

Input : str = "bbbbb"
Output: 0
Explanation: Repeated characters in the string
cannot be rearranged such that there should not
be any adjacent repeated character.
Your task :
You don't have to read input or print anything. Your task is to complete the functionrearrangeString() which takes the string as input and returns the modified string. If the string cannot be modified return "-1".
Note:The generatedoutput is 1 if the string is successfully rearranged and is 0 if rearranging is not possible.
 
Expected Time Complexity : O(NlogN), N = length of String
Expected Auxiliary Space : O(number of english alphabets)
 
Constraints :
1 <= length of string <= 104
"""

import heapq
from collections import Counter

class Solution:
    def rearrangeString(self, str):
        freq = Counter(str)
        max_heap = []
        result = []
        
        # Push characters into max_heap with negative frequencies
        for char, count in freq.items():
            heapq.heappush(max_heap, (-count, char))
        
        # Process the heap to construct the rearranged string
        while max_heap:
            count, char = heapq.heappop(max_heap)
            if result and result[-1] == char:
                return "-1"  # Impossible to rearrange
            result.append(char)
            count += 1  # Decrease frequency
            if count < 0:
                heapq.heappush(max_heap, (count, char))
        
        return ''.join(result)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str1 = input()
        solObj = Solution()
        str2 = solObj.rearrangeString(str1)
        if str2=='-1':
            print(0)
        elif sorted(str1)!=sorted(str2):
            print(0)
        else:
            for i in range(len(str2)-1):
                if str2[i]==str2[i+1]:
                    print(0)
                    break
            else:
                print(1)
        
# } Driver Code Ends