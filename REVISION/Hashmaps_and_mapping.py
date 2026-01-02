nums = [4,4,3,2,3,4,3,2,3,4,2,23,34,5,6,5,1,2,35,6,7,7,6,5,3,3,5]

def Highest_occurence(arr):
    hm={}
    max_freq=0
    for x in arr:
        if x in hm:
            hm[x]+=1
        else:
            hm[x]=1
        max_freq=max(max_freq,hm[x])
    return max_freq

print(Highest_occurence(nums))
