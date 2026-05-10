def num(n):
    if n==0:
        return
    print(n)
    return num(n-1)
    
    
num(10)