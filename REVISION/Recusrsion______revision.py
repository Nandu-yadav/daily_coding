#Back Tracking
def sum1toN(N,sum):
    if N>10:
        print(sum)
        return 1
    sum1toN(N+1,sum+N)
print(sum1toN(0,0))


def sumNto1(N,sum):
    if N==0:
        print(sum)
        return 1
    sumNto1(N-1,sum+N)
print(sumNto1(10,0))

#-------------------
#Factorial
def Factorial(n):
    if n==1 or n==0:
        return 1
    return n*Factorial(n-1)
print(Factorial(10))

def Factorial1(N):
    if N>10:
        return 1
    return N*Factorial1(N+1)
print(Factorial1(1))


#____________________________
def mergeSort(low,high,arr):
    mid=(low+high)//2
    #determining mid

    if low>=high:            # Base condition to stop 
        return
    
    mergeSort(low,mid,arr)    # first half of taken Half
    mergeSort(mid+1,high,arr) # second half of taken half
    merge(low,mid,high,arr)   # marging full Array 

def merge(low,mid,high,arr,temp):
    left =low
    right=mid+1
    
    while left<=mid and right<=high:
        if arr[left]<=arr[right]:     
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    #if any element is left in piece array
    if left<=mid:
        temp.append(arr[left])
        left+=1
    if right<=high:
        temp.append(arr[right])
        right+=1
    return temp


# #______________________________________________________________________
# def QuickSort(arr):

#     def partition(arr,low,high):
#         i=low-1
#         j=high
#         p=arr[0]
#         while(i<=j):
#             while arr[i] <= p and i<=high:
#                 i+=1
#             while(arr[j]>p and j>=low):
#                 j-=1
#             if i<j:
#                 arr[i],arr[j]=arr[j],arr[i]
#         arr[low],arr[j]=arr[j],arr[low]
#         return i+1

# def Sort(arr,low,high):
#     # Pick a Pivot
#     if low<=high:
#         p=partition(arr,low,high)
#         QuickSort(arr,low,p-1)
#         QuickSort(arr,p+1,high)
#     QuickSort(arr,0,len(arr)-1)
#     return arr

# arr=[3,1,2,5,6,8,4,0,9,7]
# print(QuickSort(arr,0,9))


def subsetSUM1(arr):
    ans=[]
    n=len(arr)
    def backtrack(i,sum,n,arr,ans):
        if i>=n:
            ans.append(sum)
            return
        #pick the element
        backtrack(i+1,sum+arr[i],n,arr,ans)   #i+1 move the pointer
        #pick the element
        backtrack(i+1,sum,n,arr,ans)

        return ans
    #call with initial conditions
    backtrack(0,0,3,arr,ans)
    return ans
arrSubsetSum=[3,1,2]
print(subsetSUM1(arrSubsetSum))

