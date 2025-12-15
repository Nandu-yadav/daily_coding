
def prime1(n):
    for i in range(2,int(math.sqrt(n))):
        if n%i==0:
            return False
    return True

def prime_factors(n):
    for i in range(2,n):
        if prime1(i):
            x=i
            while n%i==0:
                print(i)
                x=x*i