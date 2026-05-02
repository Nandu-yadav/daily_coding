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