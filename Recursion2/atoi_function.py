

def myAtoi(s: str)->int:
    i=0
    n=len(s)
    sign=1
    result=0
    INT_MAX=2**31 -1
    INT_MIN=2**31
    while i<n and (s[i]=='+' or s[i]=='-'):
        if s[i]=='-':
            sign = -1
        i+=1

    if i<n and (s[i]=='+' or s[i]=='-'):
        if s[i]=='-':
            sign=-1
        i+=1
    while i<n and s[i].isdigit():
        