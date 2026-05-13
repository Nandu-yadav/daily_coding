
#BALANCED PARATHESIS
def BalancedParathesis(string):
    open=["[","{","("]
    st=[]
    for x in string:
        if x in open:
            st.append(x)
        else:
            if len(st)==0:

                return False
            else:
                if x==']'  and st[-1]=='[':
                    st.pop()
                    
                elif x=='}'  and st[-1]=='{':
                    st.pop()
                elif x==')'  and st[-1]=='(':
                    st.pop()
                else:
                    return False
    return False

string='()[{}()])'
print(BalancedParathesis(string))

#NGE
import sys

def NGE1(arr):
    st=[]
    ans=[]
    
    for i in range(len(arr)-1,0,-1):
        # if st:
        #     if arr[i]<st[-1]:
        #         ans.append(st[-1])
        #         st.append(arr[i])
        #     else:
        #         while arr[i] >= st[-1]:
        #             st.pop()
        # else:
        #     ans.append(-1)
        while (st and arr[i] >= st[-1]):
            st.pop()
        if not st:  #if stack is empty
            ans.append(-1)
        else:       #if stack is not empty
            ans.append(st[-1])
        st.append(arr[i])

    return ans[::-1]

arrayNGE=[4,12,5,3,1,2,5,3,1,2,4,6]

print(NGE1(arrayNGE))


def NGE2(arr):
    