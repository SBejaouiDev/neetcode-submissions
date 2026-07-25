# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        interation version 
        """

        if not root:
            root = TreeNode(val)


        curr = root 
        
        while curr is not None:

            print(curr.val )
            ## go left
            if val < curr.val and curr.left is not None:
                curr = curr.left
                
            ## go right
            elif val > curr.val and curr.right is not None :
                curr = curr.right
            
            else:
                break 

        if val < curr.val:
            curr.left = TreeNode(val)
        elif val > curr.val:
            curr.right = TreeNode(val)

        
        return root
