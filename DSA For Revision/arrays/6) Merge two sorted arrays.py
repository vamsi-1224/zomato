def merge(nums1, m, nums2, n):                             #For zeros and all cases                      
    # Start merging from the back of nums1 to avoid overwriting values
    p1 = m - 1  # Pointer to the last meaningful element in nums1
    p2 = n - 1  # Pointer to the last element in nums2
    p = m + n - 1  # Pointer to the last position in nums1

    # Merge in reverse order
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]                                              # TIME COMPLEXITY 0=(M+N)
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # If there are remaining elements in nums2, copy them
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

# Test Cases:

# Example 1:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print("Output for Example 1:", nums1)  # Output: [1, 2, 2, 3, 5, 6]

# Example 2:
nums1 = [1]
m = 1
nums2 = []
n = 0
merge(nums1, m, nums2, n)
print("Output for Example 2:", nums1)  # Output: [1]

# Example 3:
nums1 = [0]
m = 0
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)
print("Output for Example 3:", nums1)  # Output: [1]





#FOR NON_ZER0
def merge(nums1, m, nums2, n):
    # If nums2 is empty, there's nothing to merge
    if n == 0:
        return

    # If nums1 has no meaningful elements, directly copy nums2 into nums1
    if m == 0:
        for i in range(n):
            nums1[i] = nums2[i]
        return

    # Two pointers for merging:
    left = m - 1  # Last meaningful element in nums1
    right = 0     # First element in nums2

    # Swap elements between nums1 and nums2 if needed
    while left >= 0 and right < n:
        if nums1[left] > nums2[right]:
            nums1[left], nums2[right] = nums2[right], nums1[left]
            left -= 1
            right += 1
        else:
            break

    # Sort nums1 and nums2
    nums1.sort()
    nums2.sort()

    # Merge sorted nums2 into the zeros of nums1
    for i in range(n):
        nums1[m + i] = nums2[i]

# Test Cases:

# Example 2:
nums1 = [1]  # nums1 with one meaningful element
m = 1
nums2 = []  # nums2 is empty
n = 0
merge(nums1, m, nums2, n)
print("Output for Example 2:", nums1)  # Output: [1]

# Example 3:
nums1 = [0]  # nums1 with no meaningful elements, 0 as placeholder
m = 0
nums2 = [1]  # nums2 has one element
n = 1
merge(nums1, m, nums2, n)
print("Output for Example 3:", nums1)  # Output: [1]




#ANOTHER PROBLEM



def merge(arr1, arr2, n, m):

    # Declare 2 pointers:
    left = n - 1
    right = 0

    # Swap the elements until arr1[left] is smaller than arr2[right]:
    while left >= 0 and right < m:
        if arr1[left] > arr2[right]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1
            right += 1
        else:
            break

    # Sort arr1[] and arr2[] individually:
    arr1.sort()
    arr2.sort()

if __name__ == '__main__':
    arr1 = [1, 4, 8, 10]
    arr2 = [2, 3, 9]
    n = 4
    m = 3
    merge(arr1, arr2, n, m)

    print("The merged arrays are:")
    print("arr1[] = ", end="")
    for i in range(n):
        print(arr1[i], end=" ")
    print("\narr2[] = ", end="")
    for i in range(m):
        print(arr2[i], end=" ")
    print()

#Output: The merged arrays are: arr1[] = 1 2 3 4 arr2[] = 8 9 10 