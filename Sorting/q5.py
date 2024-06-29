"""
Given arrival and departure times of all trains that reach a railway station. Find the minimum number of platforms required for the railway station so that no train is kept waiting.
Consider that all the trains arrive on the same day and leave on the same day. Arrival and departure time can never be the same for a train but we can have arrival time of one train equal to departure time of the other. At any given instance of time, same platform can not be used for both departure of a train and arrival of another train. In such cases, we need different platforms.

Examples:

Input: n = 6, arr[] = {0900, 0940, 0950, 1100, 1500, 1800}, 
            dep[] = {0910, 1200, 1120, 1130, 1900, 2000}
Output: 3
Explanation: There are three trains during the time 0940 to 1200. So we need minimum 3 platforms.
Input: n = 3, arr[] = {0900, 1235, 1100}, 
            dep[] = {1000, 1240, 1200}
Output: 1
Explanation: All train times are mutually exlusive. So we need only one platform
Input: n = 3, arr[] = {1000, 0935, 1100}, 
            dep[] = {1200, 1240, 1130}
Output: 3
Explanation: All 3 trains have to be their from 11:00 to 11:30
 

Note: Time intervals are in the 24-hour format(HHMM) , where the first two characters represent hour (between 00 to 23 ) and the last two characters represent minutes (this will be <= 59 and >= 0).

Expected Time Complexity: O(nLogn)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ n ≤ 50000
0000 ≤ arr[i] ≤ dep[i] ≤ 2359
"""

import atexit
import io
import sys

class Solution:
    def minimumPlatform(self, n, arrival, departure):
        # Sorting arrival and departure times
        arrival.sort()
        departure.sort()
        
        i = 0  # Pointer for arrival array
        j = 0  # Pointer for departure array
        platforms = 0  # Current number of platforms in use
        max_platforms = 0  # Maximum platforms needed at any time
        
        # Merge-like traversal of arrival and departure arrays
        while i < n and j < n:
            if arrival[i] <= departure[j]:
                platforms += 1
                i += 1
            else:
                platforms -= 1
                j += 1
            
            # Update maximum platforms needed
            max_platforms = max(max_platforms, platforms)
        
        return max_platforms

# Main driver code
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minimumPlatform(n, arrival, departure))
