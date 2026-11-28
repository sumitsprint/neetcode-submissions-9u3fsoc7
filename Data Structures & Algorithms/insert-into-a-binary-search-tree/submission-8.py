# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
    
        curr = root
        dummy = curr

        while curr:
            if val > curr.val:
                parent = curr
                

                curr = curr.right
                
                

            elif val < curr.val:
                parent = curr
               
                curr = curr.left
                

        if val > parent.val:
            parent.right = TreeNode(val) 

        else:
            parent.left = TreeNode(val)      
        return dummy                 

    
        
        
        
        