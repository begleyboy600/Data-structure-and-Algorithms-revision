class Solution:
    def longestSubstrDistinctChars(self, S):
        if not S:
            return 0
        
        charMap = {}
        max_len = 0
        left = 0

        for right in range(len(S)):
            if S[right] in charMap:
                # Move left pointer to the right of the last occurrence of S[right]
                left = max(left, charMap[S[right]] + 1)
            
            # Update the last seen position of the current character
            charMap[S[right]] = right

            # Calculate the current window size
            current_len = right - left + 1

            # Update max_len if the current window is larger
            max_len = max(max_len, current_len)
        
        return max_len
    
# Driver code
if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        S = input().strip()
        sol = Solution()
        print(sol.longestSubstrDistinctChars(S))