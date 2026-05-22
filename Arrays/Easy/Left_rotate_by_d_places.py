#optimal
def reverse(arr,l,r):
    while l<=r:
        temp=arr[l]
        arr[l]=arr[r]
        arr[r]=temp
        l+=1
        r-=1
#IMPORTANT!!
        
def RotateArray2(arr,d,l,r):
    reverse(arr,l,d-1)
    reverse(arr,d,r)
    reverse(arr,l,r)
    return arr

nums=[1,2,3,4,5,6,7,8,9]
RotateArray2(nums,3,0,8)   
print(nums)


#Brute
def RotateArray(arr,d):
    n=len(arr)
    d=d%n
    temp=[]
    for i in range(d):
        temp.append(i)
    for i in range(0,d):
        temp[i]=arr[i]
    for i in range(d,n):
        arr[i-d]=arr[i]
    for i in range(0,d):
        arr[n-d+i-1]=temp[i]
    return arr

nums=[1,2,3,4,5,6,7,8,9]
RotateArray(nums,4)     
print(nums)



#lef_rotate_by_one_place    
def LeftRotate(arr):
    n=len(arr)
    temp=arr[0]
    for i in range(1,n):
        arr[i-1]=arr[i]
    arr[n-1]=temp
    return arr

nums=[2,4,1,6,9,6,7,3]
LeftRotate(nums)           
print(nums)
