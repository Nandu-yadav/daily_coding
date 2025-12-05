
#OPTIMAL TWO pointer method
def Intersection(arr1,arr2):
    #if match move both
    #IF NOT, just move i, 
    #when i or j run of of elements , we stop
    i=0
    j=0
    n=len(arr1)
    m=len(arr2)
    result=[]

    while(i<n and j<m):
        if (arr1[i]<arr2[j]):
            i+=1
        elif (arr1[i]>arr2[j]):
            j+=1
        else:
            result.append(arr1[i])
            i+=1
            j+=1
    return result

nums1=[0,1,2,3,4,5,6]
nums2=[4,5,6,7,8,9]
print(Intersection(nums1,nums2))