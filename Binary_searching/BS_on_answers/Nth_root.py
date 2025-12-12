#Optimal
def Nth_rt_BS(n,x):
    low=0
    high=n
    ans=-1
    while(low<=high):
        mid=(low+high)//2
        if mid**x <=n:
            ans= mid
            low=mid+1
        else:
            high=mid-1

    return ans
print(Nth_rt_BS(100,3))