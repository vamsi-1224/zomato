#BRUTE FORCE SOLUTION
                                                                                        #striver sheet 
arr=[12, 35, 1, 10, 34, 1]    
n=len(arr)
arr.sort()
largest=arr[n-1]
second=arr[0]
for i in range(n):
    if arr[i]!=largest:
        second=arr[i]
print(second)                        #TIME COMPLEXITY 0(n log n )+0(n)=0(n log n )


#BETTER SOLUTION
arr=[12, 35, 1, 10, 34, 1]
largest=arr[0]
second_largest=-1
for i in range(len(arr)):
    if arr[i]>largest:
        largest=arr[i]
print(largest)
for i in range(len(arr)):
    if arr[i]>second_largest and arr[i]!=largest:
        second_largest=arr[i]
print(second_largest)
               