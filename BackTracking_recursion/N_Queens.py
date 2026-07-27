

def isSafe(row,col,board,n):
    for j in range(0,n):
        if board[row][j]=='Q':
            return False
    for i in range(0,n):
        if board[i][col]=='Q':
            return False
    for i in range(row,0,-1):
        for j in range(col,0,-1):
            if board[i][j]=='Q':
                return False
    for i in range(row,0,-1):
        for j in range(col,n):
            if board[i][j]=='Q':
                return False
    return True

def NQueens(board,row,col,n,ans):
    n=len(board[0])
    for j in range(0,n):
        if isSafe(row,col,board,n):
            board([row][j])='Q'
            NQueens(board,row+1,n,ans)
            board([row][j])='.'
    return ans

board=[]
print(NQueens(board,0,0,len(board),[]))

