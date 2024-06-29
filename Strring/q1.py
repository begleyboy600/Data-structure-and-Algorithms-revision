def isValid(s):
    components = s.split('.')

    # Check if there are exactly 4 components
    if len(components) != 4:
        return 0
    
    for comp in components:
        # Check if component is empty or has non-digit characters
        if not comp.isdigit():
            return 0
        
        # Convert to integer
        num = int(comp)

        # Check if the number is between 0 and 255
        if num < 0 or num > 255:
            return 0

        # Check for leading zeros
        if comp != '0' and comp[0] == '0':
            return 0
        
    return 1


# Driver code
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        s = input().strip()
        if isValid(s):
            print(1)
        else:
            print(0)