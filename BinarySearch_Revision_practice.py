#Basic searching Algorithm

def BinarySearch(arr,k):
    n=len(arr)
    l=0
    h=n-1
    while(l<=h):
        mid=(l+h)//2
        if arr[mid]==k:
            return mid
        elif arr[mid]>k:
            h=mid-1
        else:
            l=mid+1
    return None

arr1=[1,2,3,4,5,6,7,8,9,10,16,17,18,19,20,21]
print(BinarySearch(arr1,2))


def Binary_recursive(arr,l,h,k):
    if l>h:
        return -1
    mid=(l+h)//2
    if (arr[mid]==k):
        return mid
    elif arr[mid]>k:
        return Binary_recursive(arr,l,mid-1,k)
    else:
        return Binary_recursive(arr,mid+1,h,k)
print(Binary_recursive(arr1,0,15,2))