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
        def permute(s, chosen, visited, result):
            if len(chosen) == len(s):
                result.append("".join(chosen))
                return
            
            for i in range(len(s)):
                if visited[i] or (i > 0 and s[i] == s[i-1] and not visited[i-1]):
                    continue
                
                visited[i] = True
                chosen.append(s[i])
                permute(s, chosen, visited, result)
                chosen.pop()
                visited[i] = False
        
        # Sort the string to handle duplicates correctly
        sorted_s = ''.join(sorted(S))
        result = []
        permute(sorted_s, [], [False] * len(S), result)
        return result

# Driver code
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        S = input().strip()
        obj = Solution()
        ans = obj.find_permutation(S)
        for permutation in ans:
            print(permutation, end=" ")
        print()
