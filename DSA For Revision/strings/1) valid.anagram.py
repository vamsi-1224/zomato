#Example 1:                                                             #Neetcode and Leetcode no 241

s = "anagram", t = "nagaram"        #Output: true                
s = "rat", t = "car"          #Output: false



s1={}
t1={}
for i in s:
    if i in s1:
        s1[i]+=1
    else:
        s1[i]=1
for i in t:
    if i in t1:
        t1[i]+=1
    else:
        t1[i]=1
if s1==t1:
    print(True)
print(False)