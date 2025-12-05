def Merge(arr,low,mid,high):
    i=low
    j=mid+1
    temp=[]
    while(i<=mid and j<=high):
        if(arr[i]<arr[j]):
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1
    while (i<=mid):
        temp.append(arr[i])
    while j<=high:
        temp.append(arr[j])
    for i in range(high):
        arr[i]=temp[i]
    

nums=[2,4,1,6,9,6,7,3]
Merge(nums,0,3,7)   
print(nums)