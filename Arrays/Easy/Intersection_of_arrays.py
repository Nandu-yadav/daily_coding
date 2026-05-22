
#OPTIMAL TWO pointer method
def Intersection(arr1,arr2):
    
    i=0
    j=0                               #if match move both
    n=len(arr1)                       #IF NOT, just move i, 
    m=len(arr2)                       #when i or j run of of elements , we stop
    result=[]

    while(i<n and j<m):
        if (arr1[i]<arr2[j]):         #if arr[i] is less update i
            i+=1
        elif (arr1[i]>arr2[j]):       #if arr[j] is less update j
            j+=1
        else:
            result.append(arr1[i])    #if both equal  append to answer
            i+=1
            j+=1
    return result

nums1=[0,1,2,3,4,5,6]
nums2=[4,5,6,7,8,9]
print(Intersection(nums1,nums2))