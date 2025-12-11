#LONGEST CONSECUTIVE SEQUENCE

#BRUTE
#1 do linear search
class Solution:
    def linear_search(self,arr,num):
        for i in range(len(arr)):
            if arr[i]==num:
                return True
        return False
    def longestSequence(self,arr): 
        n=len(arr)
        if n==0:
            return 0

        longest=1
        for i in range(n):
            x=arr[i]
            cnt=1
            while self.linear_search(arr,x+1):
                x+=1
                cnt+=1
            longest =max(longest,cnt)
        return longest
    
nums = [1,1,2,3,4,5,5,2,1,3,7,8,9,0,10,11,12,13,15]
s=Solution()
print(s.longestSequence(nums))

def longest_sequence2(arr):
    n=len(arr)
    arr.sort()
    lastSmaller= float('-inf')
    cnt=0
    longest=0
    for i in range(n):
        if arr[i]-1==lastSmaller:
            cnt+=1
            lastSmaller=arr[i]
        elif arr[i]!=lastSmaller:
            cnt=1
            lastSmaller=arr[i]
        longest=max(longest,cnt)
    return longest

print(longest_sequence2(nums))

#   OPTIMAL
def longest_sequence3(arr):
    n=len(arr)
    cnt=0
    longest=0
    st=set()
    for i in range(n):
        st.add(arr[i])
    for it in st:
        
        if it-1 not in st:
            cnt=1
            x=it
        while x+1 in st:
            cnt += 1
            x += 1
        longest=max(longest,cnt)
    return longest
print(longest_sequence3(nums))

    
        

         
