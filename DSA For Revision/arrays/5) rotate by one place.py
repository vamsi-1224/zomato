nums=[1,2,3,4,5] #Output [2,3,4,5,1]                                                  #striver sheet
temp=nums[0]
for i in range(1,len(nums)):
    nums[i-1]=nums[i]
nums[len(nums)-1]=temp
print(nums)                  #TIME COMPLEXITY IS 0(n)
                             #Space complexity is 0(1)