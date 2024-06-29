"""
Given an array arr of distinct elements of size n, the task is to rearrange the elements of the array in a zig-zag fashion so that the converted array should be in the below form: 

arr[0] < arr[1]  > arr[2] < arr[3] > arr[4] < . . . . arr[n-2] < arr[n-1] > arr[n]. 

Note: Modify the given arr[] only, If your transformation is correct, the output will be 1 else the output will be 0. 

Examples

Input: n = 7, arr[] = {4, 3, 7, 8, 6, 2, 1}
Output: 1
Explanation:  After modification the array will look like 3 < 7 > 4 < 8 > 2 < 6 > 1, the checker in the driver code will produce 1.
Input: n = 5, arr[] = {4, 7, 3, 8, 2}
Output: 1
Explanation: After modification the array will look like 4 < 7 > 3 < 8 > 2 hence output will be 1.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= n <= 106
0 <= arri <= 109
"""

from typing import List

class Solution:
    def zigZag(self, n: int, arr: List[int]) -> None:
        for i in range(1, n):
            # If the current index is even and the previous element is greater than the current element,
            # or if the current index is odd and the previous element is less than the current element,
            # then swap the elements.
            if (i % 2 == 0 and arr[i - 1] > arr[i]) or (i % 2 != 0 and arr[i - 1] < arr[i]):
                arr[i - 1], arr[i] = arr[i], arr[i - 1]


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

    def isZigzag(n: int, arr: List[int]) -> bool:
        for i in range(1, n):
            if i % 2 == 0:
                if arr[i - 1] >= arr[i]:
                    return False
            else:
                if arr[i - 1] <= arr[i]:
                    return False
        return True

    t = int(input())  # number of test cases
    for _ in range(t):
        n = int(input())  # size of the array
        arr = IntArray().Input(n)  # input array
        
        obj = Solution()
        obj.zigZag(n, arr)
        
        # Check if the modified array is zigzag
        check = isZigzag(n, arr)
        
        # Additional check to verify if the array is correctly zigzagged
        flag = False
        for i in range(n):
            if arr[i] == i % 2:
                flag = False
            else:
                flag = True
                break
        
        if not flag:
            print("0")
        else:
            if check:
                print("1")
            else:
                print("0")