#Kadane's Algorithm
'''
Docstring for Arrays.lonest_subArray_loop
1. say max to be lowest number(int_min)
2. sum=0
3. sum in each case compared with int_min
4. if we get to add -ve number we dont add,cause it just decreases the sum
5.  
'''
import sys
def longestSubArray(arr):
    sum=0
    maxi= -sys.maxsize-1
    for i in range(n):
        sum=+arr[i]
        if (sum>maxi):
            maxi = sum
        if (sum< o ):
            sum=0
    return maxi

'''
Kadane's Algorithm is an efficient way to find the maximum sum of a contiguous subarray within a one-dimensional array of numbers (7:50).

Here's how it generally works:

You initialize two variables: current_sum (or sum in the video) to 0 and max_so_far (or maxi in the video) to the lowest possible number (e.g., negative infinity or INT_MIN).
You iterate through the array, adding each element to current_sum.
At each step, you compare current_sum with max_so_far and update max_so_far if current_sum is greater (14:03).
If current_sum ever becomes negative, you reset it to 0 (9:47). This is because a negative current_sum will only decrease the sum of any future subarrays it's part of, so it's better to start a new subarray from the next element.
The algorithm effectively ignores any portion of the array that would lead to a negative sum, ensuring that current_sum always represents the maximum possible sum ending at the current position. This approach results in a time complexity of O(N) and a space complexity of O(1)'''

def subarray(arr):
    n=len(arr)
    maximum= -sys.maxsize-1
    for i in range(n):
        for j in range(i+1,n):
            sum=0
            for k in range(i,j):
                sum+=arr[k]
            maximum=max(maximum,sum)
    return maximum


def subarray1(arr):
    n=len(arr)
    maximum=-sys.maxsize-1
    for i in range(n):
        sum=0
        for j in range(i+1,n):
            sum+=arr[j]
        maximum=max(maximum,sum)
    return maximum

#FOLLOW UP

def longestSubArray1(arr):
    sum=0
    maxi= -sys.maxsize-1
    for i in range(n):
        if sum==0:
            start=i
            sum=+arr[i]
            if (sum>maxi):
                maxi = sum
            if (sum< o ):
                sum=0
    return maxi