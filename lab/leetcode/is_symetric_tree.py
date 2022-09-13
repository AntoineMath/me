class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

#         (1)
#        /   \ 
#     (2)     (2) 
#     / \     / \
#   (3) (4) (4) (3)
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

def isSymetric(self, root: TreeNode) -> bool:
    return isMirror(root, root)

        
def isMirror(left: TreeNode, right: TreeNode ) -> bool:
    if left is None and right is None: return True

    if left is not None and right is not None:
        if left.val == right.val:
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)
    
    return False

print(isSymetric(root, root))