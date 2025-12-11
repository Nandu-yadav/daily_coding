


def SetMatrix(matrix):
    n=len(matrix)
    m=len(matrix[0])
    row=[0]*m
    col=[0]*n
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                row[i]=1
                col[j]=1
    for i in range(n):
        for j in range(m):
            if row[i]==1 or col[j]==1:
                matrix[i][j]=0
    return matrix

