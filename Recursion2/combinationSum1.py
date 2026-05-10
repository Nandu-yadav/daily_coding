
#combination sum 1
#any index any number of times
def CombinationSum(i,arr,target,ans,ds):
    if i==len(arr):                             #1. if length of index exceding check for target getting 0
        if target ==0:                           #if 0 append to answer
            ans.append(list(ds))
        return
        
    if arr[i]<=target:
        ds.append(arr[i])                           #3. 
        CombinationSum(i,arr,target-arr[i],ans,ds)
        ds.pop()
    
    CombinationSum(i+1,arr,target,ans,ds) 
    return ans

arr1=[2,3,4,5]
print(CombinationSum(0,arr1,8,[],[]))


#UNIQUE combinations #cannot be duplicated unless in the list,, each number may only be used duplicate combinations
#no duplicate combinations
#ALL COMBINATIONS SHOULD BE IN SORTED ORDER
arr2=[1,1,1,2,2]

def CombinationSum2(i,arr,target,ans,ds):
    if i==len(arr):                       #1check if lenght is not exceeded
        if target ==0:                    # 1. check if terget reached if reached append ds to answer and return astop further recusrsion
            ans.append(list(ds))
        return
        
    if arr[i]<=target:                   #2. if target is not reached yet,    append the indexed number to DS ,
        ds.append(arr[i])
        CombinationSum2(i+1,arr,target-arr[i],ans,ds)  # then repeat function for  not pick index for same sum
        ds.pop()                                   # remove the last added number to make it ready for another combination with i+1 index
    
    CombinationSum2(i+1,arr,target,ans,ds)     #move for i+1 th index    , to make it ready for further recursion with remaining elements
    return ans

print(CombinationSum2(0,arr2,5,[],[]))

