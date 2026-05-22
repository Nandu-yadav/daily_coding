

def LCU_BST(root,p,q):
    if root is None:
        return None
    
    
    if root.val>p.val and root.val>q.val:
        return LCU_BST(root.left,p,q)
    elif root.val<p.val and root.val<q.val:
        return LCU_BST(root.left,p,q)
    else:
        return root.val
    