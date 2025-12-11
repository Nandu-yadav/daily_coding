
def searchInsert( nums, target):
    n=len(nums)
    low,high=0,n-1
    ans=n
    while(low<=high):
        mid=(low+high)//2
        if (nums[mid]>=target):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
nums=[0,1,2,3,4,6,7,8,9]
print(searchInsert(nums,5))
