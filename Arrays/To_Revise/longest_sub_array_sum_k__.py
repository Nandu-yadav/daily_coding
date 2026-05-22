#Optimal for positives + negatives 
#Better for positives
def longestSubArray(arr,k):
    preSumMap={}
    s=0
    maxLen=0
    n=len(arr)
    for i in range(0,n):
        s +=arr[i]
        # case 1: prefix sum itself equals k (subarray from 0 to i)
        if(s ==k):
            maxLen = max(maxLen,i+1)
        # case 2: check if (s - k) exists in prefix map
        rem = s -k
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen=max(maxLen,length)
        # store prefix sum only if first time
        if s not in preSumMap:
            preSumMap[s] = i
    return maxLen
nums = [2, 4, 1, 6, 9, 6, 7, 3]
print(longestSubArray(nums, 16))


#Optimal for positives
def longestSubArray1(arr,k):
    l=0
    r=0
    n=len(arr)
    sum=0
    maxLen=0
    for r in range(n):
        sum+=arr[r]
        while(sum>k ):
            sum -=arr[l]
            l+=1
        if sum==k:
            maxLen=max(maxLen,r-l+1)
        r+=1
    return maxLen

nums=[2,4,1,6,9,6,7,3]
print(longestSubArray1(nums,16))



'''
left = 0
currentSum = 0
maxLength = 0

for right = 0 to n-1:
    currentSum += arr[right]

    while currentSum > K:
        currentSum -= arr[left]
        left += 1

    if currentSum == K:
        maxLength = max(maxLength, right - left + 1)

Sliding Window Algorithm (for Positive Numbers / Zeros)
✅ Core Idea

The main idea is to expand the subarray from the right to increase the sum and shrink it from the left when the sum exceeds K.

Because all elements are positive or zero, the sum:

only increases or stays the same when we move right

only decreases when we move left

This property makes the sliding window technique valid and optimal.

🔹 Algorithm Explanation
1️⃣ Pointers and Sum Initialization

Maintain two pointers: left and right

Maintain a variable currentSum

Initially:

left = 0

currentSum = 0

maxLength = 0

2️⃣ Move the Right Pointer (Expand Window)

Move right from 0 to n-1

Add arr[right] to currentSum

This step expands the window.

3️⃣ Shrink the Window (Left Pointer)

If currentSum > K, shrink the window:

Subtract arr[left] from currentSum

Increment left

Continue shrinking until currentSum ≤ K

This ensures the window always represents a valid candidate.

4️⃣ Check for Valid Subarray

After each adjustment:

If currentSum == K

Calculate length = right - left + 1

Update maxLength
'''

#Kadane's Algorithm
'''
lonest_subArray_loop
1. say max to be lowest number(int_min)
2. sum=0
3. sum in each case compared with int_min
4. if we get to add -ve number we dont add,cause it just decreases the sum
5.  
'''
import sys
def longestSubArraySUM(arr):
    sum=0
    maxi= -sys.maxsize-1
    n=len(arr)
    for i in range(n):
        sum=+arr[i]
        if (sum>maxi):
            maxi = sum
        if (sum< 0):
            sum=0
    return maxi

'''
Kadane's Algorithm is an efficient way to find the maximum sum of a contiguous subarray within a one-dimensional array of numbers (7:50).

Here's how it generally works:

You initialize two variables: current_sum (or sum in the video) to 0 and max_so_far (or maxi in the video) to the lowest possible number (e.g., negative infinity or INT_MIN).
You iterate through the array, adding each element to current_sum.
At each step, you compare current_sum with max_so_far and update max_so_far if current_sum is greater (14:03).
If current_sum ever becomes negative, you reset it to 0 (9:47).
 This is because a negative current_sum will only decrease the sum of any future subarrays it's part of, so it's better to start a new subarray from the next element.
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
