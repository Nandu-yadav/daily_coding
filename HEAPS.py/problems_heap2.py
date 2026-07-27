#1 Kth smallest element

#l= starting index
#r = ending index
from collections import queue
def KthSmallest(arr,k,r):
    #make a max heap for first k elements ,create a max Heap

    pq=priority_queue 

    for i in range(0,k):
        pq.append(arr[i])

    for i in range(k,r):
        if arr[i]<pq[-1]:
            pq.pop()
            pq.append(arr[i])
    ans=pq.pop[-1]
    return ans

