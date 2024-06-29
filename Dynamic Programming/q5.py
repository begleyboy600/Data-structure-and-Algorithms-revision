"""
The cost of stock on each day is given in an array A[] of size N. Find all the segments of days on which you buy and sell the stock such that the sum of difference between sell and buy prices is maximized. Each segment consists of indexes of two elements, first is index of day on which you buy stock and second is index of day on which you sell stock.
Note: Since there can be multiple solutions, the driver code will print 1 if your answer is correct, otherwise, it will return 0. In case there's no profit the driver code will print the string "No Profit" for a correct solution.

Example 1:

Input:
N = 7
A[] = {100,180,260,310,40,535,695}
Output:
1
Explanation:
One possible solution is (0 3) (4 6)
We can buy stock on day 0,
and sell it on 3rd day, which will 
give us maximum profit. Now, we buy 
stock on day 4 and sell it on day 6.
Example 2:

Input:
N = 5
A[] = {4,2,2,2,4}
Output:
1
Explanation:
There are multiple possible solutions.
one of them is (3 4)
We can buy stock on day 3,
and sell it on 4th day, which will 
give us maximum profit.

Your Task:
The task is to complete the function stockBuySell() which takes an array of A[] and N as input parameters and finds the days of buying and selling stock. The function must return a 2D list of integers containing all the buy-sell pairs i.e. the first value of the pair will represent the day on which you buy the stock and the second value represent the day on which you sell that stock. If there is No Profit, return an empty list.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)


Constraints:
2 ≤ N ≤ 106
0 ≤ A[i] ≤ 106
"""

class Solution:
    # Function to find the days of buying and selling stock for max profit.
    def stockBuySell(self, A, n):
        # To store result as pairs of buy-sell days
        result = []
        
        # Traverse the given price array
        i = 0
        while i < n - 1:
            # Find the local minima (buy day)
            while i < n - 1 and A[i + 1] <= A[i]:
                i += 1
            
            # If we reached the end, break as no further solution possible
            if i == n - 1:
                break
            
            buy = i
            i += 1
            
            # Find the local maxima (sell day)
            while i < n and A[i] >= A[buy]:
                i += 1
            
            sell = i - 1
            
            # Record this buy-sell pair
            result.append((buy, sell))
        
        return result

#{ 
 # Driver Code Starts
#Initial template for Python

def check(ans,A,p):
    c = 0
    for i in range(len(ans)):
        c += A[ans[i][1]]-A[ans[i][0]]
    if(c==p):
        return 1 
    else:
        return 0

if __name__=='__main__':
    t = int(input())
    while(t > 0):
        n = int(input())
        A = [int(x) for x in input().strip().split()]
        ob = Solution()
        ans = ob.stockBuySell(A, n)
        p = 0
        for i in range(n - 1):
            p += max(0, A[i + 1] - A[i])
        if len(ans) == 0:
            print("No Profit", end="")
        else:
            print(check(ans, A, p), end="")
        print()
        t -= 1
# } Driver Code Ends
