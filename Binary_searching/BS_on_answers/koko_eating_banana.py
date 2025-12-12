import math
import sys


def minEatingSpeed( piles, h):
    def function(arr,x):
        ans=0
        for val in arr:
            ans=ans+math.ceil(val/x)
        return ans
    
    def maxEl(nums):
        maxi=-sys.maxsize-1
        for val in nums:
            if val>maxi:
                maxi=val
        return maxi

    n=len(piles)
    low=0
    high=maxEl(piles)
    ans=high
    while (low<=high):
        mid=(low+high)//2
        total=function(piles,mid)
        if total<=h:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
piles = [3,6,7,11]
piles1= [30,11,23,4,20]
print(minEatingSpeed( piles, 8))
print(minEatingSpeed( piles1, 5),)
print(minEatingSpeed( piles1, 6),)

'''
1. low = 0 is illegal (division by zero)
Speed cannot be 0. function(piles, 0) → divides by zero → program crashes.
Correct:
low = 1
2. ans must be defined before the loop
Inside if total <= h: you assign ans = mid, but if that branch never executes in early iterations, ans is undefined at the return
ans=high (worst case)
'''