#Brute Force Solution                                                                           #striver sheet
arr = [1, 2, 3, 4, 5]
def isSorted(arr, n):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                return False

    return True               #TIME COMPLEXITY =0(N^2)


#OPTIMAL SOLUTION
arr = [1, 2, 3, 4, 5]
n=len(arr)
for i in range(1,n):
    if arr[i]<arr[i-1]:
        print(False)
print(True)                  #TIME COMPLEXITY =0(N)
