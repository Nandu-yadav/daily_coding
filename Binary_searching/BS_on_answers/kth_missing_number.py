#Brute
def kth_missing(arr,k):
    n=len(arr)
    for i in range(n):
        if arr[i]<=k:
            k+=1
        else:
            return k
    
nums=[2,3,4,7,11]
print(kth_missing(nums,5))

#Optimal
def kth_missing1(arr,k):
    n=len(arr)
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]-(mid+1)<k:   #< k not more than
            low=mid+1
        else:
            high=low-1
    return high+k+1                # or return low+k
print(kth_missing1(nums,5))