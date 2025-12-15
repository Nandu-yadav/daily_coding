#brute
#OPtimal-Euclid Algorith
def gcd(a,b):
    while(a!=b):
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
def GCD(a,b):
    if b==0:
        return a
    else:
        gcd (b,a%b)

def LCM(a,b):
    res=max(a,b)
    while True:
        if res%a==0 and res%b==0:
            return res
        res+=1
#optimal
a*b = lcm(a,b) * gcd(a,b)

