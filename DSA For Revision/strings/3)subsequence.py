def isSubsequence(s, t):
    t_iter = iter(t)
    return all(char in t_iter for char in s)


'''
# Example 1
s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))  # Output: True

# Example 2
s = "axc"
t = "ahbgdc"
print(isSubsequence(s, t))  # Output: False


'''

# method 2

def isSubsequence(s, t):
    i, j = 0, 0  # Pointers for s and t
    while i < len(s) and j < len(t):
        if s[i] == t[j]:  # If characters match, move the s pointer
            i += 1
        j += 1  # Always move the t pointer
    return i == len(s)  # If we've matched all characters in s, return True
