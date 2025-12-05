

#Brute
def TwoSum(arr,k):
    n=len(arr)
    for i in range(i+1,n):
        for j in range(i,n):
            if arr[i]+arr[j]==k:
                return  "yes"
    return "No"
#O(n)= n^2

#Better ,Hashing
class Solution:
    def twoSum(self, nums, target):
        Hash = {}  # value -> index
        
        for i in range(len(nums)):
            num = nums[i]
            moreNeeded = target - num
            
            if moreNeeded in mpp:
                return [hash[moreNeeded], i]
            
            hash[num] = i
        
        return [-1, -1]
#O(n)= NlogN


#Optimal, without map
#two pointer, first sort the array then move pointers according to the requirement of increments and decrements
 # for yes or no thing this is optimal else if (they are asking the indexes rather than jujst existance then this is not optimal as it is using 2N space for storing a temp array etcc)
 def read(n, book, target):
    left, right = 0, n - 1
    book.sort()

    while left < right:
        s = book[left] + book[right]

        if s == target:
            return "YES"
        elif s < target:
            left += 1
        else:
            right -= 1

    return "NO"

#time : O(n)= N + NlogN




