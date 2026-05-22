

prev=None

prev   =  TreeNode(None)
first  =  TreeNode(None)
sec =  TreeNode(None)

def inorder(root):

    inorder(root.left)
    
    if root is None:
        return
    
    if prev != None and root.val < prev.val:
        if not first:
            first=prev
        sec=root

    prev=root

    inorder(root.right)

    return root



def Recover_BST(root):
    inorder(root)
    first.val,sec.val   =   sec.vaval,first.val
    return root


#for constant space complexity
#ans=iteration (Morris inorder Traversal) not recursion
    
