# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        
        Traverse the tree inorder
        recursive call
        """
        res = []

        def Traversal(root):
            print(res)
            #base case:
            if root:
                Traversal(root.left)

                res.append(root.val)

                Traversal(root.right)


        Traversal(root) 
        return res