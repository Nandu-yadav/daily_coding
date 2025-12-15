#optimal using BS
#O(nlogN)TC and SC O(1)
def shipWithinDays(weights, days):
    def function(weights,cap):
        days=1
        load=0
        for i in range(len(weights)):
            if load+weights[i]>cap :
                days+=1
                load=weights[i]
            else:
                load+=weights[i]
        return days

    low=max(weights)
    high=sum(weights)
    ans= high
    while (low<=high):
        mid=(low+high)//2
        No_days=function(weights,mid)
        if No_days<=days:              #misted : dont get confused at this condition
            ans = mid
            high=mid-1                 #mistaked : also dont get confused at this condition
        else:
            low=mid+1
    return ans
