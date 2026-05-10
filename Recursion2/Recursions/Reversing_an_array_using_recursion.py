
'''
#single pointer method

def reverse(i,arr):
    n=len(arr)
    if i>=n//2:
        return 
    else:
        arr[i],arr[n-i-1]= arr[n-i-1] ,arr[i]
        reverse(i+1,arr)

nums=[2,4,1,6,9,6,7,3]
reverse(0,nums)         
print(nums)'''

'''
#Using two pointers
def Reverse1(l,r,arr):
    if l>=r:
        return
    else:
        arr[l],arr[r-1]=arr[r-1],arr[l]
        Reverse1(l+1,r-1,arr)

nums=[2,4,1,6,9,6,7,3]
n=len(nums)
Reverse1(0,n,nums)         
print(nums)
'''

#single pointer

def Reverse2(i,arr):

    if l>=r:
        return
    else:
        arr[l],arr[r-1]=arr[r-1],arr[l]
        Reverse2(l+1,r-1,arr)

nums=[2,4,1,6,9,6,7,3]
n=len(nums)
Reverse2(0,n,nums)         
print(nums)
        