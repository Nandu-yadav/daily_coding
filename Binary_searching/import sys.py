import sys
def search(arr):
    n=len(arr)
    l=0
    h=n-1
    minimum = sys.maxsize
    while(l<=h):
        mid=(l+h)//2
        if arr[l]<arr[h]:
            minimum = min(minimum,arr[l])
            break

        if (arr[l]<=arr[mid]):
            minimum = min(minimum,arr[l])
            l=mid+1
        else:
            minimum = min(minimum,arr[mid]) 
            #HERE ITS MID WE STORE NOT THE LOW , becuse mid will be the lowest the that half which is sorted
            h=mid-1
    return minimum 

nums=[7,8,9,10,11,12,-1,0,1,2]
print(search(nums))