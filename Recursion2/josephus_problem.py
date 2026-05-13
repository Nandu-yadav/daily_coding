


def josephus(n,k):
    arr=[]
    for i in range(1,n):
        arr[i]=i
    
    def helper(n,k,arr):
        if len(arr)==1:
            return arr[0]
        
        