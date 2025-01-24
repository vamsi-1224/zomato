#Bruete Solution
arr=[1,1,4,6]                                                                       #striver sheet
n=len(arr)
arr.sort()
print(arr[-1])                 #TIME COMPLEXITY IS O(n log n)


#Better solution
arr=[1,3,2,45,100,-1]
maxi=max(arr)
print(maxi)                    #TIME COMPLEXITY IS 0(n)


#OPTIMAL SOLUTION
arr=[1,1,4,6]               
largest=arr[0]
n=len(arr)
for i in range(n):
    if arr[i]>largest:
        largest=arr[i]
print(largest)                 #TIME COMPLEXITY IS 0(n)


