
n=5
s=0
for i in range(n):
    #stars
    for j in range(n-i):
        print("*",end=" ")
    #spaces
    for j in range(s ):
        print(" ",end=" ")
    #stars
    for j in range(n-i):
        print("*",end=" ")
    s+=2
    print()
s2=8
for i in range(n):
    #stars
    for j in range(i+1):
        print("*",end=" ")
    #spaces
    for j in range(s2):
        print(" ",end=" ")
    #stars
    for j in range(i+1):
        print("*",end=" ")
    s2-=2
    print()