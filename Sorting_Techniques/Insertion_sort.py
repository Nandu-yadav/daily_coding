
def insertion(arr):
    n=len(arr)
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]

nums=[2,4,1,6,9,6,7,3]
insertion(nums)           
print(nums)


"""
We start with the second element of the array as the first element is assumed to be sorted.
Compare the second element with the first element if the second element is smaller then swap them.
Move to the third element, compare it with the first two elements, and put it in its correct position
Repeat until the entire array is sorted.

"""
