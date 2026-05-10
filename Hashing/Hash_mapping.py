arr=[1,2,2,2,3,3,4,4,4,4,5,5,6,7,8,9,9,9,0,0]

def hashing(arr):
    hm={}
    max_freq=0
    for x in arr:
        if x in hm:
            hm[x]+=1
        else:
            hm[x]=1
        max_freq=max(max_freq,hm[x])
    return max_freq


print(hashing(arr))