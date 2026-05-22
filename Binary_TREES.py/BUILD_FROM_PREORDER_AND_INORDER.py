#BUILD_FROM_PREORDER_AND_INORDER

class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


def search(inorder, val,l,r):
    for i in range(l,r):
        if val==inorder[i]:
            return i
    return -1

def buildTree(preorder,inorder,preidx,l,r):
    if l>r:
            return 
    
    root = TreeNode(preorder[preidx])
    

    inidx = search(inorder,preorder[preidx], l , r )
    preidx += 1

    root.left   =  buildTree(preorder,inorder,preidx,   l,      inidx-1)
    root.right  =  buildTree(preorder,inorder,preidx,   inidx+1,      r)

    return root

preorder= [3,9,20,15,7]
inorder= [9,3,15,20,7]
preidx=0
print(buildTree( preorder , inorder , preidx , 0 , len(inorder)-1))