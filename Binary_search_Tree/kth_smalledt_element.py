

def kthsmallest(root,k):
    prevOrder=0
    def helper(root,prevOrder,k):
        if root is None:
            return -1
        
        if root.left:
            left=helper(root.left,prevOrder,k)
            if left:
                return left


        if prevOrder+1 ==k:
            return root.val
        prevOrder  +=  1


        if root.right:
            right=helper(root.right,prevOrder,k)
            if right:
                return right
        return -1
    return helper(root,prevOrder,k)

        