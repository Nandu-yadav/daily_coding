#Moore's voting Algorithm



nums = [2, 2, 2, 2, 1, 3]
#BRUTE
def Majority(arr):
    for val in arr:
        cnt=0
        for j in range(len(arr)):
            if arr[j]==val:
                cnt+=1
        if cnt>(len(arr)//2):
            return val
    return "no"

nums = [2, 2, 2, 2, 1, 3]
nums2=[4,5,4]
print(Majority(nums))

#Better HASHING
def Majority_hashing(arr):
    n=len(arr)
    hash=[0]*100
    for x in arr:
       hash[x] += 1
    for val in arr:
       if hash[val]>(n//2):
          return val
nums = [2, 2, 2, 2, 1, 3]
print(Majority_hashing(nums))








def majorityElement(self, arr: List[int]) -> int:
    cnt=0
    el=0
    for i in range(len(arr)):
        if cnt==0:
                cnt=1
                el=arr[i]
            elif arr[i]==el:
                cnt+=1
            else:
                cnt-1
        cnt1=0
        for i in range(len(arr)):
            if arr[i]==el:
                cnt1 +=1
        if cnt1 > (len(arr)/2):
            return el
        return -1
            
        