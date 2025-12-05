#Optimal for positives + negatives 
#Better for positives
def longestSubArray(arr,k):
    preSumMap={}
    s=0
    maxLen=0
    n=len(arr)
    for i in range(0,n):
        s +=arr[i]
        # case 1: prefix sum itself equals k (subarray from 0 to i)
        if(s ==k):
            maxLen = max(maxLen,i+1)
        # case 2: check if (s - k) exists in prefix map
        rem = s -k
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen=max(maxLen,length)
        # store prefix sum only if first time
        if s not in preSumMap:
            preSumMap[s] = i
    return maxLen
nums = [2, 4, 1, 6, 9, 6, 7, 3]
print(longestSubArray(nums, 16))


#Optimal for positives
def longestSubArray1(arr,k):
    l=0
    r=0
    n=len(arr)
    sum=0
    maxLen=0
    for r in range(n):
        sum+=arr[r]
        while(sum>k ):
            sum -=arr[l]
            l+=1
        if sum==k:
            maxLen=max(maxLen,r-l+1)
        r+=1
    return maxLen

nums=[2,4,1,6,9,6,7,3]
print(longestSubArray1(nums,16))
