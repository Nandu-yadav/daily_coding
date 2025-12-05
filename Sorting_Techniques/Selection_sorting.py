


def Selection(arr):
    n=len(arr)
    
    for i in range(n):
        min_index=i
        for j in range(i,n):
            if  arr[min_index]>arr[j]:
                min_index=j

        arr[min_index],arr[i]=arr[i],arr[min_index]

nums=[2,4,1,6,9,6,7,3]
Selection(nums)
print(nums)






# by repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first unsorted element.
'''
1. First we find the smallest element and swap it with the first element. This way we get the smallest element at its correct position.
2. Then we find the smallest among remaining elements (or second smallest) and swap it with the second element.
3. We keep doing this until we get all elements moved to correct position.
'''
