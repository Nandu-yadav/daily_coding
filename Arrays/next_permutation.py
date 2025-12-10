#BRUTE solution using Recursion 
#will take O(n!*n) time compexity

def Next_permutation(arr):
    n=len(arr)
    index=-1
    for i in range(n-2,0,-1):
        if arr[i]<arr[i+1]:
            index=i
            break
    if index=-1:
        arr[0:n] = arr[0:n][::-1]

    for i in range(n-1,index,-1):
        if arr[index]< arr[i]:
            arr[index],arr[i]= arr[i],arr[index]
            break
    
    
    arr[index-1:n] = arr[index-1:n][::-1]
    return arr

nums=[2,1,5,4,3,0,0]
print(Next_permutation(nums))