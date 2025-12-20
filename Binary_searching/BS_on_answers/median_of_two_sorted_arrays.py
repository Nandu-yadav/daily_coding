#Brute
def median_arrays(nums1,nums2):
    i=0
    j=0
    n=len(nums1)
    m=len(nums2) # its better initializing as n1 n2 3n etc.. than n,m,k etc..
    
    while(i<n and j<m):
        if nums1[i]<nums2[j]:
            nums3.append(nums1[i])
            i+=1
        else:
            nums3.append(nums2[j])
            j+=1
    while (i<n):
        nums3.append(nums1[i+=1])
    while (j<m): #mistake n insted of m
        nums3.append(nums2[j+=1])
    
    if (n+m)%2==0:
        return (nums3[(n+m-2)//2]+nums3[(n+m)//2])/2
    else:
        return nums3[(n+m)//2] #//  and For an odd total length, the median index is total // 2, not (total + 1) // 2.