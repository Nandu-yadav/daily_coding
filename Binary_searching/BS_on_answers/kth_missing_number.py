#Brute
def kth_missing(arr,k):
    n=len(arr)
    for i in range(n):
        if arr[i]<=k:
            k+=1
        else:
            return k
    
nums=[2,3,4,7,11]
print(kth_missing(nums,5))

#Optimal
def kth_missing1(arr,k):
    n=len(arr)
     