# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        s = []
        s.append(root)
        if not root:
            return []
        #res.append(root.val)
        while s:

            q = s.pop()
            res.append(q.val)
            print(q.val, end=" ")
            if q.right:
                s.append(q.right)
               
            
            if q.left:
                s.append(q.left)
                
    

        return res 