
def Trap(arr):
    stack=[]
    water=0
    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            mid=stack.pop()
            if not stack:
                break
            left = stack[-1]
            width=i-left-1
            bounded_height=min(arr[left],arr[i])- arr[mid]
            water += width * bounded_height

        stack.append(i)
    return water


#TWO POINTER METHOD
def Trapping_rain_water(arr):
    if not arr:
        return 0
    n=len(arr)
    maxl=0          #Declaring maxL,maxR, 
    maxR=0          # Declaring  left, right
    water=0         #intially 0 water
    l,r = 0,n-1     #
    while l<r:
        if arr[l]<arr[r]:       
            maxl=max(maxl,arr[l])
            water+= maxl-arr[l]
            l +=1
        else: #if arr[l]>arr[r]
            maxR=max(maxR,arr[r])
            water+= maxR-arr[r]
            r -=1
    return water

trap=[4,2,0,3,2,5]
print(Trapping_rain_water(trap))

'''
1. first declare all required variables
2. loop only runs till left and right cross each other
3. if left pointer is less maxL is updated and
4.   water = maxL - left pointer is used
5. if not vive versa
    right pointer is less ,it is updated, 
    formula used,  
6. pointer is updated by position
'''
