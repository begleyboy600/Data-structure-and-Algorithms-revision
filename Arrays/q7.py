"""
Given an array of size n. Find the subarray of size k that has the least average among all the subarrays of size of k. Return the index of the first element of the subarray(1-based indexing) of size k that has least average.

Examples :

Input: nums = [30, 20, 10], k = 1
Output: 3
Explanation: Subarrays of length 1 are {30}, {20}, {10}. {10} has the least average equal to 10.
Input: nums = [30, 20, 10], k = 2
Output: 2
Explanation: Subarrays of length 2 are {30, 20}, {20, 10}. {20, 10} has the least average equal to (20 + 10)/2 = 15.
Expected Time Complexity: O(n)
Expected Space Compelxity: O(1)
 

Constraints:
1 <= k <= n <= 100000
1 <= elements of array <= 1000000
"""

class Solution:
    def least_average(self, nums, k):
        n = len(nums)
        
        # Initialize variables to track the minimum average and its starting index
        min_avg = float('inf')
        min_index = 0

        # Compute the sum of the first window of size k
        current_sum = sum(nums[:k])

        # Set initial values for min_avg and min_index based on the first window
        min_avg = current_sum / k
        min_index = 0

        # Slide through the array and update min_avg and min_index
        for i in range(1, n - k + 1):
            current_sum = current_sum - nums[i - 1] + nums[i + k - 1]
            current_avg = current_sum / k

            if current_avg < min_avg:
                min_avg = current_avg
                min_index = i

         # Return the 1-based index of the first element of the subarray with the minimum average
        return min_index + 1    # Adding 1 to convert to 1-based index
    

# Driver code
if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        n, k = map(int, input().strip().split())
        nums = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.least_average(nums, k)
        print(ans)