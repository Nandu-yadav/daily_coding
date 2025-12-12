nums = [1,2,5,9]
import math
#Brute
def divisor_threshold(arr,threshold):
    maxi=max(arr)

    for i in range(1,maxi):
        sum=0
        for j in range(len(arr)):
            sum += math.ceil(arr[j]/i)
        if sum<=threshold:
            return i
#print(divisor_threshold(nums,6))
import math
#optimal
def divisor_threshold1(arr,threshold):
    maxi=max(arr)
    low=1
    high=maxi
    ans=-1
    while(low<=high):
        mid=(low+high)//2
        sum=0
        for j in range(len(arr)):
            sum += math.ceil(arr[j]/mid)
        if sum<=threshold:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

print(divisor_threshold1(nums,6))
nums1 = [44,22,33,11,1]
print(divisor_threshold1(nums1,5))
