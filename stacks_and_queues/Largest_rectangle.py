

def fuction(nums):
    st=[]
    for i in range(len(nums)):
        while st and arr[st[-1]]>arr[i]:
            element=st[-1]
            st.pop()
            nse=i 
            pse=st.empty