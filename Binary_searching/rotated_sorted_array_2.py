

def search(arr,target):
    n=len(arr)
    l=0
    h=n-1
    while(l<=h):
        mid=(l+h)//2
        
        if arr[mid]==target:
            return mid
        if arr[l]==arr[mid] and arr[mid]==arr[h]:
            l+=1
            h-=1
            continue
        elif (arr[l]<=arr[mid]):
            if (arr[l]<=target and target <= arr[mid]):
                h=mid-1
            else:
                l=mid+1
        else:
            if (arr[mid]<=target and target <= arr[h]):
                l=mid+1
            else:
                
                h=mid-1
    return -1

nums=[3,3,3,9,0,1,3,3,3,3,3,3,3,3,3,3]
print(search(nums,0))