#REDO
n=5

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range (2*i-1):
        print("*",end=" ")
    print()



'''
 for each row there are some spaces that get printed then some stars and then again some spaces giving it a final pyramidal look. For eg: In the first row (i=0) there are 4 spaces, 1 star, then again 4 spaces. In the second row (i=1) there are 3 spaces, 3 stars, then again 3 spaces so we can say that there are N-i-1 spaces, 2*i+1 stars, and then again N-i-1 spaces for each row where i is the row index. We thus simply run 3 inner loops first for printing the spaces, then the stars, and then the spaces again.'''