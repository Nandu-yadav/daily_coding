class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right



def findMin(nums):
    
    low=0
    high=len(nums)-1
    while low<high:
        mid=(low+high)//2

        if nums[low]>=nums[high]: #SURE
            if nums[mid]>=nums[low]:
                low=mid+1
            if nums[mid]<nums[low]:
                high=mid
        else:
            high=mid
    return nums[low]

nums1=[2,2,2,0,1]
print(findMin( nums1))