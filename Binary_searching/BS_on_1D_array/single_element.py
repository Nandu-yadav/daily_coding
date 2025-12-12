
def singleNonDuplicate(arr):
    n=len(arr)
    if n==1 :
        return arr[0]
    if arr[1]!=arr[0]:
        return arr[0]
    if arr[n-2]!=arr[n-1]:
        return arr[n-1]
    low=1
    high=n-2
    while (low<=high):
        mid=(low+high)//2
        if arr[mid]!=arr[mid+1] and arr[mid]!= arr[mid-1]:
            return arr[mid]
        #I am on left half and answer on right half
        if (mid%2==1 and arr[mid-1]==arr[mid]) or (mid%2==0 and arr[mid+1]==arr[mid]) :
            low=mid+1
        # mid is in right half
        else:
            high=mid-1
    return -1