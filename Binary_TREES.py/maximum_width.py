from collections import dqueue
class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


def MaxWidth(root):
    q=dqueue()
    q.push(root,0)

    maxWid=0

    while (len(q)>0):
        stIdx = q.front()