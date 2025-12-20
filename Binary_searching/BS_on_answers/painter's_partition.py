class Solution:
    def splitArray(self, arr: List[int], k: int) -> int:
        n=len(arr)
        low=max(arr)
        high=sum(arr)
        if n<k:
            return -1
        while(low<=high):
            mid=(low+high)//2
            currSum=0
            painter=1      #mistake 1 staring from 0
            for i in range(n):
                if currSum+arr[i] <= mid:
                    currSum+=arr[i]
                else:
                    currSum=arr[i]
                    painter+=1
            if painter<=k:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans