#Brute is Merge Sort

#Better is cnt0,cnt1,cnt2 and rewrite array to new


#Dutch National Flag Algorithm
# 3 pointers
    # everything from 0,low -1 will be zeros
    #everything from low to mid-1 should be 1
    #everything from mid +1 to n-1 should be 2
'''low and mid start from 0, high starts from n-1 and moves left'''
def Sorting012(arr):
    n=len(arr)
    low=0
    mid=0
    high=n-1
    while(mid<=high):
        if arr[mid]==0:
            arr[mid],arr[low]=arr[low],arr[mid]
            mid+=1
            low+=1
        elif arr[mid]==1:
            mid+=1
        elif arr[mid]==2:
            arr[mid],arr[high]=arr[high],arr[mid]
            high -=1
            mid+=1
    return arr

nums=[0,2,1,0,2,1,2,1,1,0,0,0,2,2,1,0,]
Sorting012(nums)           
print(nums)

