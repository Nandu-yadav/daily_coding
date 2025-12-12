
#Brute
def sqrt_BS(n):
    ans=-1
    for i in range(n):
        if i*i<=n:
            ans=i
        else:
            break
    return ans
print(sqrt_BS(26))


#Optimal
def Sqrt_BS(n):
    low=0
    high=n
    ans=-1
    while(low<=high):
        mid=(low+high)//2
        if mid*mid<=n:
            ans= mid
            low=mid+1
        else:
            high=mid-1

    return ans
print(Sqrt_BS(26))