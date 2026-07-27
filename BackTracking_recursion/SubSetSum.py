

#BRUTE is by bit manipulation





#OPTIMAL
def subsetSUM1(arr):
    ans=[]
    n=len(arr)
    def backtrack(i,sum,n,arr,ans):
        if i>=n:
            ans.append(sum)
            return
        #pick the element
        backtrack(i+1,sum+arr[i],n,arr,ans)   #i+1 move the pointer
        #pick the element
        backtrack(i+1,sum,n,arr,ans)

        return ans
    #call with initial conditions
    backtrack(0,0,3,arr,ans)
    return ans

arrSubsetSum=[3,1,2]
print(subsetSUM1(arrSubsetSum))


