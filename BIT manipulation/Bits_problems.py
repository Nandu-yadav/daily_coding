


'''
| Operator | Meaning     | Example       |    |        |
| -------- | ----------- | ------------- | -- | ------ |
| `&`      | AND         | `5 & 3 = 1`   |    |        |
| `        | `           | OR            | `5 | 3 = 7` |
| `^`      | XOR         | `5 ^ 3 = 6`   |    |        |
| `~`      | NOT         | `~5 = -6`     |    |        |
| `<<`     | Left shift  | `5 << 1 = 10` |    |        |
| `>>`     | Right shift | `5 >> 1 = 2`  |    |        |
'''

#1. Minimum flips to convert number
def MinFlips(a,b):
    #XOR is only operator to differentiate
    c= a ^ b
    #Count of number of set bits is the answer
    cnt= 0
    for i in range(0,31):
        if (c and (1<<i))==1:
            cnt+=1
    return cnt
print(MinFlips(15,16))

#2 Power sets
def powerSet(arr):
    subsets=1<<len(arr)
    ans=[]
    for i in range(subsets):
        list=[]
        if arr[i] and 1<<i:
            list.append(arr[i])
        ans.append(list)
    return ans


#Divide without division symbol
def divide_BIT(divident,divisor):
    dd=divident
    ds=divisor
    if dd ==ds:
        return 1
    if ds==0:
        return None
    sign=True
    while sign:
        if dd>=0 and ds<0:
            sign =False
        if dd<=0 and ds>0:
            sign =False
    dd=abs(dd) 
    ds=abs(ds)
    while dd>=ds:
        cnt=0
        while(dd>=(ds and (1<<(cnt+1)))):
            cnt+=1
    return cnt




