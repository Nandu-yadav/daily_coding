
def stars(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print()
    return 0
print(stars(5))