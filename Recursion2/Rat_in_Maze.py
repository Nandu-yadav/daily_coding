

def backtrack(mat,row,col,ds,ans,vis):
    n=len(mat)

    #BASE CONDITIONS
    #Extrme boundaries
    if  row<0 or row>n or col>n or col<0 or mat[row][col]==-1 or  mat[row][col]==0:    # If satnding point is 0
        return 
        
    # if goal reached
    if row==n and col==n:
        ans.append(ds[:]) 
        return 
    
    mat[row][col]=-1    #visited       #vis[row][col]=True


    #FOur OPTIONS 
    backtrack(mat,row+1,col,ds.append('D'),ans)    # DOWN     #if you do using visit boolean vis(matrix) will also be included in input
   
    backtrack(mat,row-1,col,ds.append('U'),ans)  # UP

    backtrack(mat,row,col+1,ds.append('R'),ans)  # RIGHT
   
    backtrack(mat,row,col-1,ds.append('L'),ans,)  # LEFT
    
    

    mat[row][col]=1      #UNVISIT    #vis[row][col]=False
    return ans


def getPath(mat):
    ans=[]
    ds=''
    n=len(mat)
    # for i in range(n):
    #     for j in range(n):
    #         vis[i][j]=False
    vis=[]
    return backtrack(mat,0,0,ds,ans)  #vis not included

    