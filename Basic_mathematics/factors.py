def factors(n):
    for i in range(2,n):
        if n%i==0:
            print(i)
            if i!=n%i:
                print(n/i)
    return 0
import math
def factors(n):
    for i in range(2,int(math.sqrt(n))):
        if n%i==0:
            print(i)
    for i in range(int(math.sqrt(n),2,-1)):
                if n%i==0:
                    print(n/i)    
    return 0