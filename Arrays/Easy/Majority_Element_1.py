#Moore's voting Algorithm



nums = [2, 2, 2, 2, 1, 3]
#BRUTE
def Majority(arr):
    for val in arr:
        cnt=0
        for j in range(len(arr)):
            if arr[j]==val:
                cnt+=1
        if cnt>(len(arr)//2):
            return val
    return "no"

nums = [2, 2, 2, 2, 1, 3]
nums2=[4,5,4]
print(Majority(nums))

#Better HASHING
def Majority_hashing(arr):
    n=len(arr)
    hash=[0]*100
    for x in arr:
       hash[x] += 1
    for val in arr:
       if hash[val]>(n//2):
          return val
nums = [2, 2, 2, 2, 1, 3]
print(Majority_hashing(nums))


def majorityElement(arr: List[int]) -> int:
    cnt=0
    el=0
    for i in range(len(arr)):
        if cnt==0:
                cnt=1
                el=arr[i]
        elif arr[i]==el:
            cnt+=1
        else:
            cnt-1
        cnt1=0
        for i in range(len(arr)):
            if arr[i]==el:
                cnt1 +=1
        if cnt1 > (len(arr)/2):
            return el
        return -1
            


#Moore’s Voting Algorithm (also called the Boyer–Moore Majority Vote Algorithm)
'''is an efficient method to find the majority element in an array.

What is a Majority Element?

A majority element is an element that appears more than ⌊n/2⌋ times in an array of size n.

Example:
[2, 2, 1, 2, 3, 2, 2] → majority element is 2

Key Idea (Intuition)

If an element appears more than half the time, it cannot be completely canceled out by other elements.

The algorithm works by pairing different elements and canceling them.

The remaining candidate (if a majority exists) will be the majority element.

Algorithm Steps
Step 1: Find a Candidate

Initialize:

candidate = None

count = 0

Traverse the array:

If count == 0, set candidate = current element

If current element == candidate, increment count

Else, decrement count

At the end of this step, candidate is a potential majority element.

Step 2: Verify the Candidate (Important!)

Count the occurrences of the candidate.

If it appears more than n/2 times → it is the majority element.

Otherwise → no majority element exists.
'''  