from collections import deque



# Tree Node Definition
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Create Binary Tree
root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


# Inorder Traversal
def inorder(root):

    if root is None:
        return

    inorder(root.left)
    print(root.val)
    inorder(root.right)


# Postorder Traversal
def postorder(root):

    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.val)


# Preorder Traversal
def preorder(root):

    if root is None:
        return

    print(root.val)
    preorder(root.left)
    preorder(root.right)


# Level Order Traversal (BFS)
def levelOrder(root):
    #Base condition
    if root is None:
        return
    #assign a queue
    q = deque([root])

    while q:
        node = q.popleft()
        print(node.val)
        #append children
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


# DFS Template
def dfs(root):

    if root is None:
        return
    print(root.val)

    dfs(root.left)
    dfs(root.right)


# Count Nodes
class Solution(object):
    def countNodes(self, root):

        if root is None:
            return 0

        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        return 1 + left + right


# Function Calls
print("Inorder:")
inorder(root)

print("\nPreorder:")
preorder(root)

print("\nPostorder:")
postorder(root)

print("\nLevel Order:")
levelOrder(root)

sol = Solution()
print("\nTotal Nodes:", sol.countNodes(root))