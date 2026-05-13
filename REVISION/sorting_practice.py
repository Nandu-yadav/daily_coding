
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


def QuickSort(arr):

    low=0
    high=len(arr)
    pivot=low











    
    
    