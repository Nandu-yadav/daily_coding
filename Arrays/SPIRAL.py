# 1 to check the interpretstion skills
# 2  

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    n=len(matrix)
    m=len(matrix[0])
    left=0
    right=m-1
    top=0
    bottom=n-1
    ans=[]
    while(left<=right and top<=bottom):
        for i in range(left,right+1):
            ans.append(matrix[top][i])
        top+=1
        for j in range(top,bottom+1):
            ans.append(matrix[j][right])
        right-=1
        if (top<=bottom):
            for k in range(right,left-1,-1):
                ans.append(matrix[bottom][k])
            bottom -=1
        if (left<=right):
            for l in range(bottom,top-1,-1):
                ans.append(matrix[l][left])
            left+=1
    return ans


'''
Your logic is close, but there are three critical bugs:

Loop boundaries incorrect

Using range(left, right) misses the last element; spiral requires range(left, right + 1).

Same issue for vertical loops.

Wrong indices in last loop

You used matrix[left][l] instead of matrix[l][left].

Incorrect reverse-direction ranges

Example: for bottom row, you must include both ends.'''
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        left, right = 0, m - 1
        top, bottom = 0, n - 1
        ans = []

        while left <= right and top <= bottom:

            # Traverse top row
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            # Traverse right column
            for j in range(top, bottom + 1):
                ans.append(matrix[j][right])
            right -= 1

            # Traverse bottom row (if still valid)
            if top <= bottom:
                for k in range(right, left - 1, -1):
                    ans.append(matrix[bottom][k])
                bottom -= 1

            # Traverse left column (if still valid)
            if left <= right:
                for l in range(bottom, top - 1, -1):
                    ans.append(matrix[l][left])
                left += 1

        return ans
'''
