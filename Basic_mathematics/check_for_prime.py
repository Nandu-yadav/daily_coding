

def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(prime(5))

import math
#only loop till sqrt(n)
def prime1(n):
    for i in range(2,int(math.sqrt(n))):
        if n%i==0:
            return False
    return True
print(prime1(5))