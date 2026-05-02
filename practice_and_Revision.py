

nums=[6,8,3,2,7,9,0,1,4,5]

#Selection


def selection(nums):
    n=len(nums)
    for i in range(0,n):         #mins it is i till N and j till N, 
        mini=i
        for j in range(i+1,n):   # start from i+1
            if nums[j]<nums[mini]:
                mini=j
            temp=nums[j]
            nums[j]=nums[mini]
            nums[mini]=temp
    return nums

#print(selection(nums))

#Bubble Sort
def Bubble(nums):
    n=len(nums)
    for i in range(0,n):          
        for j in range(1,n):     #this is from 1 to n    not starting from 0 or end with n-1
            if nums[j-1]>nums[j]: 
                temp=nums[j]
                nums[j]=nums[j-1]
                nums[j-1]=temp
    return nums
#print(Bubble(nums))


def Insertion(nums):
    n=len(nums)
    for i in range(1,n):          
        j=i    #I take one element and insert it into its correct place in the sorted left part 
        while (j>0 and nums[j]<nums[j-1]):
            temp=nums[j]
            nums[j]=nums[j-1]
            nums[j-1]=temp
            j-=1
    return nums
#print(Insertion(nums))

#Merge sort

def MS(nums,low,high):
    mid=(low+high)//2
    if low>=high:
        return
    MS(nums,low,mid)
    MS(nums,mid+1,high)
    merge(nums,low,mid,high)

    return nums

def merge(nums,low,mid,high):
    l=low
    r=mid+1
    temp=[]
    while(l<=mid and r<=high):
        if nums[l]<=nums[r]:
            temp.append(nums[l])
            l+=1
        else:
            temp.append(nums[r])
            r+=1
    while(l<=mid):
        temp.append(nums[l])
        l+=1
    while( r<=high):
        temp.append(nums[r])
        r+=1


    for i in range(len(temp)):   #critical steps
        nums[low + i] = temp[i]   #Both 
#print(MS(nums,0,9))


#Quick sort

def QuickSort(nums):
    n=len(nums)
    low=0
    high=n-1
    pivot=0
    for i in range(1,n):
        if nums[i]<nums[pivot]:
            nums[i],nums[pivot]=nums[pivot],nums[i]
    return nums


#Largest element in an array

def LargestArray(arr):
    maxi=arr[0]
    for i in range(len(arr)):
        maxi=max(maxi,arr[i])
    return maxi
#print(LargestArray(nums))

def S_LargestArray(arr):
    maxi=arr[0]
    s_l=arr[0]
    for i in range(len(arr)):
        maxi=max(maxi,arr[i])
    for i in range(len(arr)):
        if arr[i]!=maxi and arr[i]>s_l:
            s_l=arr[i]
    return s_l
#print(S_LargestArray(nums))

sortedNums=[1, 2, 3, 4, 5, 6, 7, 7, 7, 8]
#Check if an array is sorted
def CheckSorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True
#print(CheckSorted(sortedNums))

#REMOVE DUPLICATES
#Brute
def RemoveDuplicates(arr):
    seen=set()
    for x in arr:
        if x not in seen:
            seen.add(x)
    return seen
#print(RemoveDuplicates(sortedNums))
#OpTIMAL
def RemoveDuplicates1(arr):
    i=0
    for j in range(1,len(arr)):
        if arr[i]!=arr[j]:
            arr[i]=arr[j] 
            i+=1
    return arr
print(RemoveDuplicates1(sortedNums))

#MOVE zeros to the end

def MoveZeros(arr):
    n=len(arr)
    i=0
    for j in range(n):
        if arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    return arr

zeros=[1,0,4,0,4,0,2,0,5,0,0,0,5]
print(MoveZeros(zeros))

#UNION
nums11=[1,2,3,4,5,6,7]
nums12=[4,5,6,9,0,11]

def Union(arr1,arr2):
    m=len(arr1)
    n=len(arr2)
    for x in arr2:
        if x not in arr1:
            arr1.append(x)
    return arr1

print(Union(nums11,nums12))

#MISSING NUMBER
def MissingN(arr):
    n=len(arr)
    # #Brute
    # hash=[0]*n
    # for i in range(n):
    #     hash[arr[i]]=1
    # for i in range(1,n):
    #     if hash[i]==0:
    #         return i
    #SUM
    sum=0
    k=0
    while k<n:
        sum+=arr[k]
        k+=1
    return ((n+1)*(n+2)/2)- sum

numsM=[1,2,3,4,6,7,8]
print(MissingN(numsM))  

#Maximum Consecutive Ones
def Max1s(arr):
    cnt=0
    maxi=0
    for x in arr:
        if x==1:
            cnt+=1
            maxi=max(cnt,maxi)
        else:
            cnt=0
    return maxi
max1s=[1,1,1,1,0,0,1,1,0,0,1,1,0]
print(Max1s(max1s))

#problem : Find number that appears twice once and other twice
def Once(arr):
    n=len(arr)
    hash=[0]*n
    for x in arr:
        hash[x]+=1
    for x in arr:
        if hash[x]==1:
            return x
once=[1,1,2,3,3,4,4,5,5,6,6]
print(Once(once))

#Longest SubArray with sum K(only positives)
#Brute n3 n
# subarray=[1,2,3,1,1,1,1,4,2,3]
# def Longest_subArray1(arr,k):
#     n=len(arr)
#     #PREFIX SUM METHOD
#     cnt=0
#     maxi=0
#     sumk=0
#     for i in range(n):
#         #
# print(Longest_subArray1(subarray,3))

#longest sub array sum with Negatives







        
#TWO SUM
def TwoSum(arr,k):
    #two pointer
    i=0
    j=len(arr)-1
    while i<j:
        sum=arr[i]+arr[j]
        if sum>k:
            j-=1
        elif sum<k:
            i+=1
        else:
            return i,j
    return None
numsS=[1,2,3,4,5,6,7,8,10]
print(TwoSum(numsS,15)) 

#SOrt 1s ,2s, 0s
def sort012(arr):
    cnt1,cnt2,cnt0=0,0,0
    for x in arr:
        if x==0:
            cnt0+=1
        elif x==1:
            cnt1+=1
        else:
            cnt2+=1
    res=[0]*cnt0 + [1]*cnt1 + [2]*cnt2
    return res
arr012=[1,0,1,0,2,0,2,0,1,2,1,2,0,1,2]
#print(sort012(arr012))

def sort012Optimal(arr):
    i,j=0,0
    k=len(arr)-1
    while (j<=k):
        if  arr[j]==0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j+=1
        elif arr[j]==2:
            arr[k],arr[j]=arr[j],arr[k]
            k-=1
        else:
            j+=1
    return arr
print(sort012Optimal(arr012))



#majority element >n/2 times:
#BRUTE : HASHING
def majority_element(arr):
    n=len(arr)
    hash={}
    for y in arr:
        hash[y]=hash.get(y,0)+1#.....................IMPORTANT LINE
    for k in hash:
        if hash[k]>=n//2:
            return k
arrME=[1,2,1,2,1,2,1,2,1,2,2]
print(majority_element(arrME))

#MOore's Voting Algorithm
def majority_elementOpt(arr):
    el=arr[0]
    cnt=0
    for x in arr:
        if cnt==0:
            cnt+=1
            el=x
        elif el==x:
            cnt+=1
        else:
            cnt-=1        
    return el
print(majority_elementOpt(arrME))


#Kadane's Algorithm
def Kadanes(arr):
    sum=0
    maxi=0
    cnt=0
    for x in arr:
        sum+=x
        if sum<0:
            sum=0
            maxi=max(maxi,sum)
            cnt=0
        else:
            cnt+=1
            maxi=max(maxi,sum)
    return maxi
arr_Kadane=[-2,-3,4,-1,-2,1,5,-3]

print(Kadanes(arr_Kadane))

#Majority element n//3
def Majority2(arr):
    el1=0
    el2=0
    return el1,el2
arr_M3=[1,1,1,2,2,2,3,3]


#Best time to BUY and SELL STOCKS
def STOCKS(arr):
    mini=arr[0]
    profit=0
    for i in range(1,len(arr)):
        cost= arr[i] - mini
        profit=max(profit,cost)
        mini=min(arr[i],mini)
    return profit
arr_stock=[7,1,5,3,7,6,4]
print(STOCKS(arr_stock))

#LEADER NUMBERS
def Leader(arr):
    res=[]
    maxr=0
    n=len(arr)
    for i in range(n-1,0,-1):
        if arr[i]>maxr:
            res.append(arr[i])
        maxr=max(maxr,arr[i])
    return res
arr_leaders=[10,22,12,3,0,6]
print(Leader(arr_leaders))

#Longest consecutive sequence
def LongestCS(arr):
    