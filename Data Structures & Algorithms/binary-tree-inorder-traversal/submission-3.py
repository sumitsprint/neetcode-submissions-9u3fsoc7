# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r=[]
        def ino(node):
            if node is None:
                return
            
            ino(node.left)
            r.append(node.val)
            ino(node.right)
        ino(root)    
        return r
                        
            
                
        