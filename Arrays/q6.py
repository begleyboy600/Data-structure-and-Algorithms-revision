"""
Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.


Example 1:

Input:
N = 4, K = 6
arr[] = {1, 5, 7, 1}
Output: 2
Explanation: 
arr[0] + arr[1] = 1 + 5 = 6 
and arr[1] + arr[3] = 5 + 1 = 6.

Example 2:

Input:
N = 4, K = 2
arr[] = {1, 1, 1, 1}
Output: 6
Explanation: 
Each 1 will produce sum 2 with any 1.

Your Task:
You don't need to read input or print anything. Your task is to complete the function getPairsCount() which takes arr[], n and k as input parameters and returns the number of pairs that have sum K.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 <= N <= 105
1 <= K <= 108
1 <= Arr[i] <= 106
"""

class Solution:
    def getPairsCount(self, arr, n, k):
        count = 0
        hash_map = {}

        # Traverse through each element in the array
        for num in arr:
            # Calculate the complement needed to reach K with the current number
            complement = k - num

            # If the complement exists in the hashmap, it means we have found pairs
            if complement in hash_map:
                count += hash_map[complement]

            # Update the hashmap with the current number
            if num in hash_map:
                hash_map[num] += 1
            else: 
                hash_map[num] = 1
        
        return count
    
# Driver code
def main():
    tc = int(input().strip())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

if __name__ == '__main__':
    main()