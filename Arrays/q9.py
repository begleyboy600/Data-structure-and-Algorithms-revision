"""
Given an array arr of size n which contains elements in range from 0 to n-1, you need to find all the elements occurring more than once in the given array. Return the answer in ascending order. If no such element is found, return list containing [-1]. 

Note: Try and perform all operations within the provided array. The extra (non-constant) ) space needs to be used only for the array to be returned.

Examples:

Input: arr[] = {0,3,1,2}, n = 4
Output: -1
Explanation: There is no repeating element in the array. Therefore output is -1.
Input: arr[] = {2,3,1,2,3}, n = 5
Output: 2 3 
Explanation: 2 and 3 occur more than once in the given array.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).

Constraints:
0 <= arr[i] <= n-1, for each valid i
1 <= n <= 105
"""

from typing import List

class Solution: 
    def duplicates(self, n: int, arr: List[int]) -> List[int]:
        result = []
        for i in range(n):
            index = arr[i] % n
            arr[index] += n
        
        for i in range(n):
            if arr[i] // n > 1:
                result.append(i)

        if not result:
            return[-1]
        
        return sorted(result)
    

if __name__ == "__main__":
    class IntArray:
        def __init__(self) -> None:
            pass
        
        def Input(self, n: int) -> List[int]:
            arr = [int(i) for i in input().strip().split()]  # array input
            return arr
        
        def Print(self, arr: List[int]) -> None:
            for i in arr:
                print(i, end=" ")
            print()

    t = int(input())  # number of test cases
    for _ in range(t):
        n = int(input())  # size of the array
        arr = IntArray().Input(n)  # input array
        
        obj = Solution()
        res = obj.duplicates(n, arr)
        
        IntArray().Print(res)