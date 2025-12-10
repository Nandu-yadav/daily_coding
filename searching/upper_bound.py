def upper_bound(arr,x):
    low=0
    n=len(arr)
    high=n-1
    ans=0
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]>x:         #CHANGE HERE only difference between lower bound and upper bound
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
nums=[0,1,2,3,4,6,7,8,9]
print(upper_bound(nums,5))