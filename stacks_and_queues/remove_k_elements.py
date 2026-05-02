
def removeKdigits(str, k):
    n=len(str)
    st=[]
    for i in range(n):
        while (st and k>0 and (int(st[-1]) > int(str[i]) )):
            st.pop()
            k-=1
        st.append(str[i])
    while (k>0):
        st.pop()
        k-=1
    if (st== False):
        return 0
    res=""
    while (st):
        res=res+st[-1]
        st.pop()
    while (len(res)!=0 and res[-1]=='0'):
        res=res[:-1]
    res=res[::-1]
    return res if res else "0"
