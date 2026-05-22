
def Merge_BSTs(root1,root2):


    arr1=inorder(root1)
    arr2=inorder(root2)

    temp=merge(arr1,arr2)

    return Build_BST(temp,0,len(temp)-1)

#function 1:
def inorder(root,ans=[]):
    if root is None:
        return None
    inorder(root.left)
    if root.val:
        ans.append(root.val)
    inorder(root.right)
    return ans
#function 2 : Merge tWO sorted Arrays
def Merge(arr1,arr2):
    i=0
    j=0
    n=len(arr1)
    ans=[]
    while i<len(arr1) and j< len(arr2):

        if arr1[i]<arr2[j]:
            ans.append(arr1[i])
            i+=1
        else:
            ans.append(arr2[j])
            j+=1
    while i<n:
        ans.append(arr1[i])
        i+=1
    while j<len(arr2):
        ans.append(arr2[j])
        j+=1
    return ans

#function 3 : build BST from Inorder
def Build_BST(temp,l,r):

    if l>r:
        return
    mid=(l+r)//2
    
    root.left= TreeNode(Build_BST(temp,l,mid-1))
    root=TreeNode(temp[mid])
    root.right= TreeNode(Build_BST(temp,mid+1,r))

    return root



