

#Set Matrix zero
matset0=[[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]
#Brute solution is n cube , your travesrse matrix then traverse whole row and column for each zero and it is one more n in worst case

def MarkRow(i,n):
    for i in range(n):
        if mat[i][j]!=0:
            mat[i][j]=-1

def MarkCol(j,n):
    for i in range(n):
        if mat[i][j]!=0:
            mat[i][j]=-
def setMat0(mat,n):
    for i in range(n):
        for j in range(i,n):
            if mat[i][j]==0:
                MarkRow(i,n)
                MarkCol(j,n)
print(matset0,4)
#OPTIMAL
#optimal
def setMat01(mat,n):
    arrR=[1]*n
    arrC=[1]*n
    for i in range(n):
        for j in range(i,n):
            if mat[i][j]==0:
                arrR[i]=0
                arrC[j]=0
    for i in range(n):
        for j in range(i,n):
            if arrR[i]==0:
                mat[i][j]=0
            if arrC[j]==0:
                mat[i][j]=0
    return mat
print(setMat01(matset0,4))

#---------------------------------------------------------------------------------------------------------------

#Rotate matrix 90degrees
matR=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def reverse(arr,n):
    i=0
    j=n-1
    while(i<j):
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr

def rotateMatrix(mat,n):
    for i in range(n):
        for j in range(i,n):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
        reverse(mat[i],n)
    return mat
print(rotateMatrix(matR,4))

#------------------------------------------------------------------------------------------------------------------------------------------
#SPIRAL MATRIX

def SpiralMatrix(mat,n):
    ans=[]
    top,bottom=0,n-1
    left,right=0,n-1
    while(top<=bottom or left<=right):
        for i in range(left,right):
            ans.append(mat[top][i])
        top+=1
        for i in range(top,bottom):
            ans.append(mat[i][right])
        right-=1
        if top<=bottom:
            for i in range(right,left,-1):
                ans.append(mat[bottom][i])
            bottom-=1
        if left<=right:
            for i in range(right,left,-1):
                ans.append(mat[i][left])
            left+=1
    return mat
matR=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(SpiralMatrix(matR,4))