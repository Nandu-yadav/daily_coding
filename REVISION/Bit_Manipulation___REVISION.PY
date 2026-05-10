
print(2)

#coNVERT TO BINARY
def dec2Binary(n):
    n=int(n)
    res=" "
    while n!=1:
        if n%2==1:
            res+="1"
        else:
            res+='0'
        n=n/2
    return res
print(dec2Binary(13))

def Bin2Dec(bin):
    n=len(bin)
    sum=0
    for i in range(n):
        sum+= (2**(n-i) ) * int(bin[i])
    return sum
print(Bin2Dec("1101"))


#------------------------------------------------------------------------------------

#swap 2numbers