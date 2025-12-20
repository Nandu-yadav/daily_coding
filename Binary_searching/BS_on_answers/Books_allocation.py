'''
Problem Statement: Given an array ‘arr of integer numbers, ‘ar[i]’ represents the number of pages in the ‘i-th’ book. There are a ‘m’ number of students, and the task is to allocate all the books to the students.
Allocate books in such a way that:

Each student gets at least one book.
Each book should be allocated to only one student.
Book allocation should be in a contiguous manner.
You have to allocate the book to ‘m’ students such that the maximum number of pages assigned to a student is minimum. If the allocation of books is not possible. return -1

'''
def Book_allocation(arr,m):
    n=len(arr)
    low=max(arr)
    high=sum(arr)
    ans=-1
    if m>n:
        return -1
    while(low<=high):
        mid=(low+high)//2
        collection=0
        student=0
        for i in range(n):
            if arr[i]+collection<=mid:
                collection+=arr[i]
            else:
                collection=arr[i]
                student+=1
        if student<m:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

arr= [12, 34, 67, 90] #n = 4, m = 2
arr1= [25, 46, 28, 49, 24] # n = 5, m = 4
print(Book_allocation(arr,2))
print(Book_allocation(arr1,4))
        
