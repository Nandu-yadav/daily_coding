

def Asteroid(arr):
    st=[]
    n=len(arr)
    for i in range(n):
        if arr[i]>0:
            st.append[ar[i]]
        else:
            while st and st[-1]>0 and st[-1]<abs(arr[i]):
                st.pop()
        if sr and st[-1]==abs(arr[i]):
            st.pop()
        elif (not st) or st[-1]<0:
            st.push(arr[i])
    return st



