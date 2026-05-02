


def Next_greatest(arr):
    n=len(arr)
    nge=[]
    st=[]
    for i in range(n-1,0):
        while (st and st[-1]<=arr[i]):
            st.pop()
        if st.empty():
            nge[i]=-1
        else:
            nge.append(st[-1])
        st.append(arr[i])
    return nge
nums=[4,12,5,3,1,2,5,3,1,2,4,6]
print(Next_greatest(nums))
 


