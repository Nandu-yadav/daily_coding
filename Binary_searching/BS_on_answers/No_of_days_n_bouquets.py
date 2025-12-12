import sys
import math
def possible(arr,n,m,k):
    cnt=0
    noBs=0
    for val in arr:
        if val<=n:
            cnt+=1
        else:
            noBs+=cnt//k
            cnt=0           #cutoff if condition is not met
    noBs+=cnt//k             #dont forget to add at thr end
    return noBs>=m

def no_min_days_for_bouqet(arr,m,k): #k=adjacent flowers m=no. of bouqets
    maxVal=-sys.maxsize-1
    minVal=sys.maxsize
    
    if len(arr)<m*k:
        return -1                 #important
    for val in arr:
        minVal=min(minVal,val)
        maxVal=max(maxVal,val)
    low=minVal
    high=maxVal
    ans=high
    while(low<=high):
        mid=(low+high)//2
        if possible(arr,mid,m,k):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

flowers= [1,10,3,10,2]
flowers1=[1,10,3,10,2]
flowers2=[7,7,7,7,12,7,7]
print(no_min_days_for_bouqet(flowers,3,1))
print(no_min_days_for_bouqet(flowers1,3,2))
print(no_min_days_for_bouqet(flowers2,3,2))
        
