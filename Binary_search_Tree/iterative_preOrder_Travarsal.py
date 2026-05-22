

def preOrder(root):
    preorder=[]
    if root is None:
        return root
    
    st=[]
    st.append(root)
    while st:
        root=st[-1]
        preorder.append(root.val)
        st.pop()


        if root.right:
            st.append(root.right)
        if root.left:
            st.append(root.left)
    return preorder