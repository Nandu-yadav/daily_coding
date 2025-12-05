def stars(n):
    for i in range(n,0,-1):
        for j in range(i):
            print(j,end=" ")
            i=i-1
        print()
    return 0

print(stars(5))