

#Brute
def TwoSum(arr,k):
    n=len(arr)
    for i in range(i+1,n):
        for j in range(i,n):
            if arr[i]+arr[j]==k:
                return  "yes"
    return "No"
#O(n)= n^2

#Better , Hashing

def twoSum(nums, target):
    mpp = {}  # value -> index
    
    for i in range(len(nums)):
        num = nums[i]
        moreNeeded = target - num
        
        if moreNeeded in mpp:
            return hash[moreNeeded], i #returning the indices
        
        hash[num] = i   #appening the num and its index no matter what
    
    return [-1, -1]
#O(n)= NlogN


#Optimal, without map
#two pointer, first sort the array then move pointers according to the requirement of increments and decrements
 # for yes or no thing this is optimal else if (they are asking the indexes rather than just existance then this is not optimal as it is using 2N space for storing a temp array etcc)





