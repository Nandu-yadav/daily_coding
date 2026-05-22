
class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def SumTree(root):
    #return sum of tree at the end

    if root is None:
        return 0
    
    left= SumTree(root.left)
    right= SumTree(root.right)
    root.data +=  left+right
    return root.val