"""
Given two strings of lowercase alphabets and a value K, your task is to complete the given function which tells if  two strings are K-anagrams of each other or not.

Two strings are called K-anagrams if both of the below conditions are true.
1. Both have same number of characters.
2. Two strings can become anagram by changing at most K characters in a string.

Example:

Input:
str1 = "fodr", str2="gork"
k = 2
Output:
1
Explanation: Can change fd to gk
Your Task:
Since this is a function problem, you don't need to take any input. Just complete the given function areKAnagrams that returns true if the strings can be turned into K-anagrams, else return false.

Constraints:
1 ≤ length of String ≤ 105
1 ≤ K ≤ length of String
"""

class Solution:
    def areKAnagrams(self, str1, str2, k):
        if len(str1) != len(str2):
            return False
        
        # Initialize frequency arrays for characters 'a' to 'z'
        freq1 = [0] * 26
        freq2 = [0] * 26
        
        # Populate frequency arrays
        for char in str1:
            freq1[ord(char) - ord('a')] += 1
            
        for char in str2:
            freq2[ord(char) - ord('a')] += 1
            
        # Calculate number of differences
        differences = 0
        for i in range(26):
            differences += abs(freq1[i] - freq2[i])
            
        # Check if differences are within K
        return differences <= k


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        k = int(input())
        ob = Solution()
        if ob.areKAnagrams(arr[0], arr[1], k):
            print(1)
        else:
            print(0)
# } Driver Code Ends