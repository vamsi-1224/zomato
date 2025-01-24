#Example 1:                                                 #Neet code      leet code 20

#Input: 
s = "()"

#Output: true

#Example 2:

#Input: 
s = "()[]{}"

#Output: true

#Example 3:

#Input: 
s = "(]"

#Output: false

#Example 4:

s = "([])"

#Output: true



stack=[]
hash={"{":"}","(":")","[":"]"}
for i in s:
    if i in hash:
        stack.append(i)
    elif stack and i==hash[stack[-1]]:
        stack.pop()
    else:
        print(False)
if len(stack)==0:
    print(True)
else:
    print(False)
