def stars(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end=" ")
            i=i-1
        print()
    return 0

print(stars(5))

#for i in range(n,0,-1):
#learnt that this n,0,-1 symbols will be there
