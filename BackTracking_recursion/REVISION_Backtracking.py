

def  SubsetsII(arr):
    #total 2**n
    ans=[]
    ds=[]
    n=len(arr)
    def helper(arr,ans,ds,i):

        if i>=n:
            ans.append(ds[:])
            return
        ds.append(arr[i]) 
        helper(arr,ans,ds,i+1)
        ds.pop()
        idx=i+1
        while idx<=n and arr[i]==arr[idx-1]: #important step
            idx += 1
        helper(arr,ans,ds,idx) #TS =O(nlogn + 2**n *n)

        return ans
    return helper(arr,ans,ds,0)

array=[1,2,2,2,3,3]
print(SubsetsII(array)) 

#PERMUTAIONS

def permutations(arr):
    ans=[]
    
    n=len(arr)
    def helper(arr,idx,ans):
        if idx==n:
            print(arr)
            return 
        for i in range(idx,n):
            arr[idx],arr[i]=arr[i],arr[idx]
            helper(arr,idx+1,ans)
            arr[i],arr[idx]=arr[idx],arr[i]
        return []
    return helper(arr,0,ans)

arr_perm=[1,2,3]
print(permutations(arr_perm))