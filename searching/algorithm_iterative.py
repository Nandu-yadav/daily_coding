
def iteratiiiiive_BS(arr,x):
    l=0
    h=len(arr)-1
    while (l<=h):
        mid = (l+h)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            h=mid-1
        else:
            l=mid+1
    return -1