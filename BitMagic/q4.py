"""
Given an array arr[] of N positive integers. Find an integer denoting the maximum XOR subset value in the given array arr[].

Example 1:

Input : 
N = 3
arr[] = {2, 4, 5}
Output : 7
Explanation : 
The subset {2, 5} has maximum 
subset XOR value.
Example 2 :

Input : 
N= 3
arr[] = {9, 8, 5}
Output : 13
Explanation : 
The subset {8, 5} has maximum 
subset XOR value.
Your Task :
You don't need to read input or print anything. Your task is to complete the function maxSubsetXOR() which takes the array and an integer as input and returns the maximum subset XOR value.
 
Expected Time Complexity : O(N*Log(max(arr[i])))
Expected Auxiliary Space : O(1)
 
Contraints :
1 <= N <= 105
1 <= arr[i] <= 106
"""

class Solution:
    def maxSubsetXOR(self, arr, N):
        max_xor = 0
        mask = 0
        
        # We iterate over each bit position from 30 down to 0
        for i in range(30, -1, -1):
            mask |= (1 << i)  # set the i-th bit in mask
            
            prefix_set = set()
            current_xor = max_xor | (1 << i)  # candidate max_xor with i-th bit set
            
            for num in arr:
                prefix_set.add(num & mask)  # consider only the most significant bits up to i
                
            for prefix in prefix_set:
                if (current_xor ^ prefix) in prefix_set:
                    max_xor = current_xor
                    break
        
        return max_xor

# Driver code
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        obj = Solution()
        print(obj.maxSubsetXOR(arr, n))
