#Basic searching Algorithm

def BinarySearch(arr,k):
    n=len(arr)
    l=0
    h=n-1
    while(l<=h):
        mid=(l+h)//2
        if arr[mid]==k:
            return mid
        elif arr[mid]>k:
            h=mid-1
        else:
            l=mid+1
    return None

arr1=[1,2,3,4,5,6,7,8,10,16,17,18,19,20,21]
print(BinarySearch(arr1,2))


def Binary_recursive(arr,l,h,k):
    if l>h:
        return -1
    mid=(l+h)//2
    if (arr[mid]==k):
        return mid
    elif arr[mid]>k:
        return Binary_recursive(arr,l,mid-1,k)
    else:
        return Binary_recursive(arr,mid+1,h,k)
print(Binary_recursive(arr1,0,15,2))

#lower Bound
def LowerBound(arr,k):
    l=0
    h=len(arr)-1
    while(l<=h):
        mid=(l+h)//2
        if arr[mid]>=k:
            h=mid-1
            ans=mid         #IMportant line
        else:
            l=mid+1
    return ans

print(LowerBound(arr1,12))

def UpperBound(arr,k):
    l=0               #element greater than or equal to target
    h=len(arr)-1
    while(l<=h):
        mid=(l+h)//2
        if arr[mid]>k:        #importnat note no much difference
            h=mid-1    
        else:
            l=mid+1
    return l
print(UpperBound(arr1,9))


#insert position
def InsertP(arr,k):
    l=0
    h=len(arr)-1
    while(l<=h):
        mid=(l+h)//2
        if arr[mid]>=k:
            h=mid-1
            ans=mid         #Important line
        else:               #Maybe an answer but not sure as checking others a well
            l=mid+1
    return ans+1

#Floor and ceiling problem

#Find the first and last occurance of an element in sorted array
def FirstAndLast(arr,k):
    l=0
    h=len(arr)-1
    while(l<=h):
        mid=(l+h)//2
        if arr[mid]>=k:
            ans=mid
            h=mid-1
        else:
            l=mid+1
    l=0
    h=len(arr)-1
    while(l<=h):
        mid=(l+h)//2
        if arr[mid]>k:
            h=mid-1
        else:
            l=mid+1
    return ans,mid,mid-ans

arr2=[1,2,3,4,5,6,7,8,10,10,10,10,10,16,17,18,19,20,21]
#print(FirstAndLast(arr2,10))

#method 2 for above
def countBS(arr,k):
    l=0
    h=len(arr)-1
    while(l<=h):
        mid=(l+h)//2
        #if arr[mid]>k: #incomplete



#Search in a rotated sorted array
#Search and Sorted means Binary search : hidden HINT
'''Identify the sorted half first
How to identify?
check low>mid 
''' 
def RotatedSortedArray(arr,k):
    l=0
    h=len(arr)-1
    while(l<=h):
        mid=(l+h)//2
        if arr[l]<=arr[mid]: #left sorted
            if arr[l]<=k and k<=arr[mid]:
                h=mid-1
            else:
                l=mid+1
        else:
            if arr[mid]<=k and k<=arr[h]:#
                l=mid+1
            else:
                h=mid-1
    return mid
arrRS=[17,18,19,20,21,1,2,3,4,5,6,7,8,10,16]
print(RotatedSortedArray(arrRS,19))

#find SquareRoot of a Number
def SrootBS(n):
    l=0
    h=n
    while(l<=h):
        mid=(l+h)//2
        if mid*mid==n:
            return mid
        elif mid*mid>=n:
            h=mid-1
        else:
            l=mid+1
    return -1
print(SrootBS(25))

#find Nth_Root of a Number
def NrootBS(n,p):
    l=0
    h=n
    while(l<=h):
        mid=(l+h)//2
        if mid**p==n:
            return mid
        elif mid**p>=n:
            h=mid-1
        else:
            l=mid+1
    return -1
print(NrootBS(125,3))

#Important
#Minimum number of days to make M Bouquets K adjacent flowers
def Possible(arr,day,m,k):
    cnt=0
    noOfB=0
    for x in arr:
        if x<=day:
            cnt+=1
        else:
            noOfB+=(cnt/k)
            cnt=0
        noOfB+=(cnt/k)
    return noOfB>=m

def Bloom(arr,m,k):
    l=min(arr)
    h=max(arr)
    while(l<=h):
        mid=(l+h)//2
        if Possible(arr,mid,m,k):
            ans=mid
            h=mid-1
        else:
            l=mid+1
    return ans

arrBloom=[7,7,7,7,13,11,12,7 ]
print(Bloom(arrBloom,2,3))


