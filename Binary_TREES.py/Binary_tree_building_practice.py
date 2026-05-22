

from collections import deque

#Node making

class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


#Create Binary Tree
root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)

root.left.left=TreeNode(4)
root.left.right=TreeNode(5)


# Inorder Traversal
def Inorder(root):

    if root is None:
        return
    Inorder(root.left)
    print(root.val)
    Inorder(root.right)

#post order

def postorder(root):
    if root==None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)
    
#pre Order
def preorder(root):
    if root==None:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

#level order BFS

def levelorderBFS(root):
    if root==None:
        return
    
    q=deque([root])

    while q:
        node=q.popleft()
        print(node.val)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)



#DFS

def DFS(root):
    if root==None:
        return
    print(root.val)

    DFS(root.left)
    DFS(root.right)
#---------------------------------------------------------------------------------------------------------------------------------------------


#COunt Nodes

class Solution(object):
    def countNode(self,root):
        if root is None:
            return 0
        
        left=self.countNode(root.left)
        right=self.countNode(root.right)

        return 1+left+right
    

ind=-1
def preOrder(arr):
    ind+=1
    if arr[ind]==-1:
        return
    
    root=TreeNode(arr[ind])
    root.left=preOrder(arr)
    root.right=preOrder(arr)

    return root

def inOrder(arr):
    ind+=1
    if arr[ind]==-1:
        return
    
    root=TreeNode(arr[ind])
    root.left=preOrder(arr)
    root.right=preOrder(arr)

    return root