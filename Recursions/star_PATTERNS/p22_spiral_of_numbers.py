n=4

for i in range(2*n-1):
    for j in range(2*n-1):
        top    =i
        left   =j
        down   =2*n-1-1-i
        right  =2*n-1-1-j
        print(n-min(min(top,down),min(left,right)),end=" ") #LOGIC...!!!
    print()

"""
DISTANCES FROM center:
Top    =i
left   =j
bottom =2n-1-1-i
right  =2n-1-1-j
"""