
def Quick_sort(arr,l,r):
    n=len(arr)
    pivot=arr[0]
    
    if (l<=r):
        def partition(arr,r,l):
            pivot=arr[l]
            i=l
            j=r
            while(i<j):
                while (arr[i]<=arr[pivot] and i<=r):
                    i+=1
                while (arr[j]>=arr[pivot] and j<=l+1):
                    j-=1

                    arr[i],arr[j]=arr[j],arr[i]
                arr[j],arr[l]=arr[l],arr[j]

                    

        

        