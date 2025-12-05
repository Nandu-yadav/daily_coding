
def LeftRotate(arr):
    n=len(arr)
    temp=arr[0]
    for i in range(1,n):
        arr[i-1]=arr[i]
    arr[n-1]=temp
    return arr

nums=[2,4,1,6,9,6,7,3]
LeftRotate(nums)           
print(nums)
