


def Next_greatest(arr):
    n=len(arr)
    nge=[]
    st=[]
    for i in range(n-1,-1,-1):
        while (st and st[-1]<=arr[i]):
            st.pop()
        if not st:
            nge.append(-1)
        else:
            nge.append(st[-1])

        st.append(arr[i])
    return nge[::-1]
nums=[4,12,5,3,1,2,5,3,1,2,4,6]
print(Next_greatest(nums))



#NGE 2
def NGE2(arr):
    n=len(arr)
    nge=[]
    st=[]
    for i in range(2*n-1,-1,-1):
        while (st and st[-1]<=arr[i%n]):
            st.pop()
        if i<n:
            if not st: #if empty
                nge.append(-1) #-1
            else:
                nge.append(st[-1])  #else Top
                
        st.append(arr[i%n])
    return nge[::-1]

nums1=[2,10,12,1,11]
print(NGE2(nums))
print(NGE2(nums1))



