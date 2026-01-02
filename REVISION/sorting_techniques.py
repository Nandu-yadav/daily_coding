nums=[2,5,4,7,3,9,4,7,3,1,8,0]

def selection(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
print(selection(nums))

def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
print(bubble(nums))

def insertion(arr):
    n=len(arr)
    for j in range(1,n):
        if arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
    return arr
print(insertion(nums))

#Quick Sort
def Quick(arr):
    n=len(arr)
    for i in range(n):
        