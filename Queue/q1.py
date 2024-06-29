"""
Implement a Stack using two queues q1 and q2.

Example 1:

Input:
push(2)
push(3)
pop()
push(4)
pop()
Output: 2 4
Explanation:
push(2) the stack will be {2}
push(3) the stack will be {2 3}
pop()   poped element will be 3 the 
        stack will be {2}
push(4) the stack will be {2 4}
pop()   poped element will be 4  
Example 2:

Input:
push(2)
pop()
pop()
push(3)
Output: 2 -1
Your Task:

Since this is a function problem, you don't need to take inputs. You are required to complete the two methods push() which takes an integer 'x' as input denoting the element to be pushed into the stack and pop() which returns the integer poped out from the stack(-1 if the stack is empty).

Expected Time Complexity: O(1) for push() and O(N) for pop() (or vice-versa).
Expected Auxiliary Space: O(1) for both push() and pop().

Constraints:
1 <= Number of queries <= 100
1 <= values of the stack <= 100
"""

#User function Template for python3
from queue import Queue

# Function to push an element into stack using two queues.
def push(x):
    global q1, q2
    q1.put(x)

# Function to pop an element from stack using two queues.
def pop():
    global q1, q2
    if q1.empty():
        return -1
    
    # Move all elements except the last one to q2
    while q1.qsize() > 1:
        q2.put(q1.get())
    
    # Get the last element from q1 (which is the top of the stack)
    top_element = q1.get()
    
    # Swap q1 and q2
    q1, q2 = q2, q1
    
    return top_element

# Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        q1 = Queue()
        q2 = Queue()
        n = int(input())
        a = list(map(int, input().strip().split()))
        i = 0
        while i < len(a):
            if a[i] == 1:
                push(a[i+1])
                i += 1
            else:
                print(pop(), end=" ")
            i += 1
        print()
