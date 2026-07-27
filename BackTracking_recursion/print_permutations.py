
#  IMPORTANT NOTe    ans.append(list(ds)) mentioning list is compulsory if not     ans.append(ds[:])
def print_Permutations(arr):
    n=len(arr)
    ans=[]
    ds=[]
    n=len(arr)
    freq={}
    for i in range(0,n):
        freq[i]=0
    def backtrack(arr,n,ds,ans,freq):
        if len(ds)==n:
            ans.append(list(ds))
            return
        for i in range(0,n):
            if freq[i]==0:
                #choose
                ds.append(arr[i])
                freq[i]=1
                #backtrack
                backtrack(arr,n,ds,ans,freq) 
                #UNCHOOSE
                freq[i]=0
                ds.pop()
        return ans    
    return backtrack(arr,n,ds,ans,freq)


array=[1,2,3]
print(print_Permutations(array))


