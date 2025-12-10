#ITERATIVE
def iterative_BS(arr,x):
    l=0
    n=len(arr)
    h=n-1
    while (l<=h):
        mid = (l+h)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            h=mid-1
        else:
            l=mid+1
    return -1

#RECURSIVE
def recursive_binary(arr,low,high,target):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    elif target>arr[mid]:
        return recursive_binary(arr,mid+1,high,target)
    else:
        return recursive_binary(arr,low,mid-1,target)

nums=[0,1,2,3,4,5,6,7,8,9]
print(recursive_binary(nums,0,len(nums)-1,9))
print(iteratiiiiive_BS(nums,9))
    