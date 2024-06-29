"""
Given a set of n nuts & bolts. There is a one-on-one mapping between nuts and bolts. You have to Match nuts and bolts efficiently. Comparison of a nut to another nut or a bolt to another bolt is not allowed. It means the nut can only be compared with the bolt and the bolt can only be compared with the nut to see which one is bigger/smaller.
The elements should follow the following order: { !,#,$,%,&,*,?,@,^ }

Note: Make all the required changes directly in the given arrays, output will be handled by the driver code.

Examples

Input: n = 5, nuts[] = {@, %, $, #, ^}, bolts[] = {%, @, #, $ ^}
Output: 
# $ % @ ^
# $ % @ ^
Explanation: As per the order # should come first after that $ then % then @ and ^. 
Input: n = 9, nuts[] = {^, &, %, @, #, *, $, ?, !}, bolts[] = {?, #, @, %, &, *, $ ,^, !}
Output: 
! # $ % & * ? @ ^
! # $ % & * ? @ ^
Explanation: We'll have to match first ! then  # , $,  %,  &,  *,  @,  ^,  ? as per the required ordering.
Expected Time Complexity: O(n(logn))
Expected Auxiliary Space: O(log(n))

Constraints:
1 <= n <= 9
The arrays 'nuts' and 'bolts' can only consist of the following elements: {'@', '#', '$', '%', '^', '&', '?', '*', '!'}.
All the elements of arrays 'nuts' and 'bolts' should be unique.
"""

class Solution:
    def partition(self, arr, low, high, pivot):
        left = low
        for i in range(low, high + 1):
            if arr[i] < pivot:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1
            elif arr[i] == pivot:
                arr[i], arr[high] = arr[high], arr[i]
                i -= 1
        arr[left], arr[high] = arr[high], arr[left]
        
        return left
    
    def matchPairs(self, n, nuts, bolts):
        self.match(nuts, bolts, 0, n - 1)
    
    def match(self, nuts, bolts, low, high):
        if low < high:
            # Choose the last bolt as pivot for nuts partition
            pivot_index = self.partition(nuts, low, high, bolts[high])
            # Use the partitioned nuts element as pivot for bolts partition
            self.partition(bolts, low, high, nuts[pivot_index])
            
            # Recursively match the left and right parts
            self.match(nuts, bolts, low, pivot_index - 1)
            self.match(nuts, bolts, pivot_index + 1, high)



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(n, nuts, bolts)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
