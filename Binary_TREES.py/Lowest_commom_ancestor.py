
#lowest_common ancestor
#LEETCODE 236

class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


def LCA(root,p,q):
    # if node1 in left sub tree  and node2 in right subtree:
    # return root
    # elif if node2 in left sub tree  and node1 in right subtree:
    # return root
    if root==None:
        return
    if root==p or root==q:
        return root
    
    left=LCA(root.left,p,q)
    right=LCA(root.right,p,q)

    if left and right:
        return root
    elif left:
        return left
    elif right:
        return right
