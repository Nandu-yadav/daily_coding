#Declaring a binary node


class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        for val in inorder:

'''   
def Build_BST(arr,l,h):

    if l>h:
        return
    mid=(l+h)//2
    root= TreeNode(arr[mid])

    root.left=   Build_BST(arr,l,mid-1)
    root.right=  Build_BST(arr,mid+1,h)

    return root

inorder=[1,2,3,4,5,6,7,8,9,10]

print(Build_BST(inorder,0,9))
'''

# def inorder(root):
#     if root is None:
#         return
    
#     inorder(root.left)
#     print(root)
#     inorder(root.right)
    
# print(inorder(Build_BST(inorder,0,9)))


#INSERT

