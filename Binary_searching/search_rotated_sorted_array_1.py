#why binary here, because theres search and sorted words given

def search(arr,target):
    n=len(arr)
    l=0
    h=n-1
    while(l<=h):
        mid=(l+h)//2
        if arr[mid]==target:
            return mid
        if (arr[l]<=arr[mid]):
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

nums=[7,8,9,0,1,2,3,4,5,6]
print(search(nums,0))


#brute solution is simply the linear search