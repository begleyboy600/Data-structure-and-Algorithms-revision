"""
Given an array A[] of size N and a positive integer K, find the first negative integer for each and every window(contiguous subarray) of size K.

 

Example 1:

Input : 
N = 5
A[] = {-8, 2, 3, -6, 10}
K = 2
Output : 
-8 0 -6 -6
Explanation :
First negative integer for each window of size k
{-8, 2} = -8
{2, 3} = 0 (does not contain a negative integer)
{3, -6} = -6
{-6, 10} = -6
 
Example 2:
Input : 
N = 8
A[] = {12, -1, -7, 8, -15, 30, 16, 28}
K = 3
Output :
-1 -1 -7 -15 -15 0 
 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function printFirstNegativeInteger() which takes the array A[], its size N and an integer K as inputs and returns the first negative number in every window of size K starting from the first till the end. If a window does not contain a negative integer , then return 0 for that window.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(K)

Constraints:
1 <= N <= 105
-105 <= A[i] <= 105
1 <= K <= N

"""

from collections import deque

def printFirstNegativeInteger(A, N, K):
    result = []
    dq = deque()
    
    for i in range(N):
        # Remove indices from deque that are out of current window
        if dq and dq[0] <= i - K:
            dq.popleft()
        
        # Add current index if A[i] is negative
        if A[i] < 0:
            dq.append(i)
        
        # If the current window is fully formed
        if i >= K - 1:
            if dq:
                result.append(A[dq[0]])
            else:
                result.append(0)
    
    return result

def main():
    T = int(input().strip())
    
    while T > 0:
        n = int(input().strip())
        A = list(map(int, input().strip().split()))
        k = int(input().strip())
        
        result = printFirstNegativeInteger(A, n, k)
        for num in result:
            print(num, end=" ")
        print()
        
        T -= 1

if __name__ == "__main__":
    main()
