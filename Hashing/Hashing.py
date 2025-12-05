'''
nums = [2, 4, 1, 6, 9, 6, 7, 3]
n = len(nums)

# frequency array of size 13 filled with zeros
freq = [0] * 13

# build frequency
for x in nums:
    freq[x] += 1

# queries
q = int(input())
for _ in range(q):
    number = int(input())
    print(freq[number])

'''

def hashing(arr):
    n=len(arr)
    hash=[0]*1000

    for i in range(n):
        hash[arr[i]]+=1
    
    q=int(input())
    for i in range(q):
        number=int(input())
        print(hash[number])

nums = [2,4,1,6,9,6,4,4,4,3,2,1,1,2,3,4,7,3]
hashing(nums)






#As you learn something CODE IT!! immediately
'''
there's high chance for you to forget
even if you dont understand on listening multiple times 
may nt understand'''



