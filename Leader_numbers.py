
#OPtimal
import sys
def Leaders(arr):
    n=len(arr)
    ans=[]
    maxn= -sys.maxsize -1
    for i in range(n-1,0,-1):
        if arr[i] >maxn:
            ans.append(arr[i])
            maxn=arr[i]
    return ans

nums = [2, 1, 6, 9, 6, 7, 4, 3]
print(Leaders(nums))

def Leaders_brute(arr):
    n=len(arr)
    ans=[]
    for i in range(n):
        for j in range(i,n):
            leader=True
            if arr[i]<arr[j]:
                leader=False
                break
        if leader:
            ans.append(arr[i]) 
    return ans

nums = [2, 1, 6, 9, 6, 7, 4, 3]
print(Leaders_brute(nums))

#1. learn to use flags or else it will print the element everytime the condition is true (greater)
#2. it will loop till end no need  to add last element again