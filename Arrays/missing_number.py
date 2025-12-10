#Brute solution O(n^2)  space-O(1)
def missingNumber1(arr):
    n = len(arr)
    for i in range(n + 1):     # must check from 0 to n
        found = False
        for val in arr:
            if val == i:
                found = True
                break
        if not found:
            return i


#Better solution
def missingNumber(nums):
    n = len(nums)
    hashh = [0] * (n + 1)

    for x in nums:
        hashh[x] = 1

    for i in range(n + 1):
        if hashh[i] == 0:
            return i

#OPTIMAL
def missingNumber1(nums):
   n=len(arr)
   sum=n*(n+1)/2
   s2=0
   for val in nums:
      s2+=val
    return sum-s2

nums=[9,6,4,2,3,5,7,0,1]
print(missingNumber1(nums))