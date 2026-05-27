# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        #dfs algo 
        stack = [root]
        visted = []


        while stack:

            s = stack.pop()
            temp = s.right
            s.right = s.left
            s.left = temp


            if s.left: 
                stack.append(s.left)
            if s.right: 
                stack.append(s.right)

            
        return root 

        #recursively call the function to check left and right children

