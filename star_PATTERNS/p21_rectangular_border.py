n=5

for i in range(n):
    for j in range(n):
        if (j==0 or i==0 or j==(n-1) or i==(n-1)) :
            print("*",end="")
        else:
            print(" ",end="")
    print()


#end="\n" adds a newline after printing.
#every print() moves to the next line
'''
end=""
Do NOT move to the next line.
Print the next output immediately after this one on the same line.
'''
#end=" "  : creates space between things in line