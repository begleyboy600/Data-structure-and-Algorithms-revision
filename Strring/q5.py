"""
Given a string S. The task is to print all unique permutations of the given string that may contain dulplicates in lexicographically sorted order. 

Example 1:

Input: ABC
Output:
ABC ACB BAC BCA CAB CBA
Explanation:
Given string ABC has permutations in 6 
forms as ABC, ACB, BAC, BCA, CAB and CBA .
Example 2:

Input: ABSG
Output:
ABGS ABSG AGBS AGSB ASBG ASGB BAGS 
BASG BGAS BGSA BSAG BSGA GABS GASB 
GBAS GBSA GSAB GSBA SABG SAGB SBAG 
SBGA SGAB SGBA
Explanation:
Given string ABSG has 24 permutations.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function find_permutation() which takes the string S as input parameter and returns a vector of string in lexicographical order.

Expected Time Complexity: O(n! * n)
Expected Space Complexity: O(n! * n)

Constraints:
1 <= length of string <= 5
"""

class Solution: 
    def find_permutation(self, S):
        def permute(s, l, r, results):
            if l == r:
                results.add(''.join(s))
            else:
                for i in range(l, r + 1):
                    s[l], s[i] = s[i], s[l]
                    permute(s, l + 1, r, results)
                    s[l], s[i] = s[i], s[l]
        
        results = set()
        permute(list(S), 0, len(S) -1, results)
        return sorted(results)
    
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.find_permutation(S)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends
    