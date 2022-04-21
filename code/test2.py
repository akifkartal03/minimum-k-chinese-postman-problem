
"""
def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Driver code to test above
arr = [64, 34, 40,25, 12, 22, 101, 0, 11, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")

"""


arr = [64, 34, 40,25, 12, 22, 10, 0, 11, 90,64]
arr2 = [40,34]
arr2.reverse()
print(arr2)




#print(sublistExists(arr,arr2))