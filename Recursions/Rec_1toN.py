
def num(i,n):
    if i>n:
        return
    print(i)
    return num(i+1,n)
    
num(1,10)