# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        ## if find 
        else:
            #
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                current_node  = root.left 
                while current_node.right:
                    current_node = current_node.right
                root.val = current_node.val
                root.left = self.deleteNode(root.left, current_node.val)
        return root




