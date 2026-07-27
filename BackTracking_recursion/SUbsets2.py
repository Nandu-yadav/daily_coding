
#Produce all subsets , should not be duplicates
def subset_2_(ind,ds,arr,ans):
    ans.append(ds)
    for i in range(ind,len(arr)):   
        ans.append(ds)     #the three important lines to eliminate duplicates
        if ind!=i and arr[i]==arr[i-1]:
            continue

        ds.append(arr[i])
        subset_2_(i+1,ds,arr,ans)
        
        ds.pop()
        
    return ans
#TC (2^n) *n
#SC (s^n) * k
arrSubsets=[1,2,2,2,3,3]
print(subset_2_(0,[],arrSubsets,[]))
