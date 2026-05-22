

#Brute TS:O(n^2)  Sc:O(1)      Double looping
def majority_element_n3(arr):
    n=len(arr)
    ans=set()
    for i in range(n):
        cnt=0
        for j in range(n):
            if arr[j]==arr[i]:
                cnt+=1
        if cnt>=n/3:
            ans.add(arr[i])
    st=[]
    for val in ans:
        st.append(val)
    return st


nums=[1,1,2,3,1,1,2,2,2]
print(majority_element_n3(nums))

#Better- Hashing
from collections import Counter
def majority_element(arr):
    n=len(arr)
    ans=[]
    mpp = Counter()
    for i in range(n):
        mpp[arr[i]]+=1
        if mpp[arr[i]]==n//3:
            ans.append(arr[i])
    return ans
print(majority_element(nums))

'''def majorityElement(arr):
    n=len(arr)
    num= None
    cnt=0
    for val in arr:
        if cnt==0:
            num=val
        cnt = cnt + 1 if val == num else cnt - 1
    return num
print(majorityElement(nums))
'''
import sys
def MajorityElement_optimal(arr):
    n=len(arr)
    cnt1=0
    cnt2=0
    el1= -sys.maxsize-1
    el2= -sys.maxsize-1
    for i in range(n):
        if cnt1==0 and el2!=arr[i]:
            cnt1=1
            el1=arr[i]
        elif cnt2==0 and el1!= arr[i]:
            cnt2=1
            el2=arr[i]
        elif arr[i]==el1:
            cnt1+=1
        elif arr[i]==el2:
            cnt2+=1
        else:
            cnt1-=1
            cnt2-=1
    ls=[]
    cnt1=0
    cnt2=0
    for i in range(n):
        if el1==arr[i]:
            cnt1+=1
        if el2==arr[i]:
            cnt2+=1
    mini=n//3+1
    if cnt1>=mini:
        ls.append(el1)
    if cnt2>=mini:
        ls.append(el2)
    ls.sort()
    return ls

print(MajorityElement_optimal(nums))
