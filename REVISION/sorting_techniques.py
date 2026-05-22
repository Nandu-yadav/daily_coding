nums=[2,5,4,7,3,9,4,7,3,1,8,0]

def selection(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
print(selection(nums))

def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
print(bubble(nums))

def insertion(arr):
    n=len(arr)
    for j in range(1,n):
        if arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
    return arr
print(insertion(nums))


def merge(low,mid,high,arr):
    i=low
    j=mid+1
    temp=[]                     # mistake 1

    while i<=mid and j<=high:       
        if arr[i]<arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1
 
    while i<=mid:
        temp.append(arr[i])
        i+=1
    
    while j<=high:
        temp.append(arr[j])
        j+=1
    for k in range(low,high+1): ##mistake 2
        arr[k]=temp[k-low]

def mergeSort(low,high,arr,n):
    if low>=high:
        return
    mid=(low+high)//2             
    
    mergeSort(low,mid,arr,n)
    mergeSort(mid+1,high,arr,n)
    merge(low,mid,high,arr)
    return arr

MergeSortarr=[9,8,7,6,5,4,3,2,2,4,1]
print(mergeSort(0,len(MergeSortarr)-1,MergeSortarr,10))



#QUICK SORT

def QuickSort(arr):

    pivot=0
    low=1
    high=len(arr)-1

    
    
    