
def lower_bound(arr,x):
    n=len(arr)
    ans=n
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if (arr[mid]>=x):        #CHANGE HERE only difference between lower bound and upper bound
            high=mid-1
            ans=mid
        else:
            low=mid+1
    return ans
nums=[0,1,2,3,4,6,7,8,9]
print(lower_bound(nums,5))

#  SHORTCUT//
#  in C++
#  lb=lower_bound(arr.begin(),arr.end(),x)