preorder=[]
bound=preorder[-1]
def preOrder_BST(preorder,idx,bound):

    if len(preorder) >= idx or preorder[idx] > bound :
        return None
    
    root=TreeNode(preorder[idx])
    idx+=1
    root.left  =  preOrder_BST(preorder,idx,root.val)
    root.right =  preOrder_BST(preorder,idx,bound)

    return root

