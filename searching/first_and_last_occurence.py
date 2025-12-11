
#naive approach
#Leanear search
def first_last(arr,x):
    first=-1
    last=-1
    for i in range(len(arr)):
        if arr[i]==x:
            if first == -1:
                first=i
            last=i
    if first == -1:
        return -1 
    return[first,last]
arr = [1,2,3,3,3,4,5]
x = 3
print(first_last(arr, x))   

#BINARY SEARCH
#lower bound arr[i]>=x
#upper_bound arr[i]>x
def first_last1(arr,x):
    def lower_bound(arr,x):
        n=len(arr)
        ans=n
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if (arr[mid]>=x):        #CHANGE HERE only difference between lower bound and upper bound
                high=mid-1
                ans=mid
            else:
                low=mid+1
        return ans
    def upper_bound(arr,x):
        n=len(arr)
        ans=n
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if (arr[mid]>=x):        #CHANGE HERE only difference between lower bound and upper bound
                high=mid-1
                ans=mid
            else:
                low=mid+1
        return ans
    

