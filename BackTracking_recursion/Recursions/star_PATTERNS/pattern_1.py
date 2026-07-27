
def stars(n):
    for i in range(1,n):
        for j in range(n):
            print("*",end=" ")
        print()

print(stars(5))
#print() adds a newline (\n) after printing.
#end=" "  You replace the default newline with a space.