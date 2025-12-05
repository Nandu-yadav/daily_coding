
def repeat(text,n):
    if n==0:
        return 0
    else:
        print(text)
    return repeat(text,n-1)

repeat("Nandu",3)