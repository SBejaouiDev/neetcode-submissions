# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def maxDepth(root) -> int:
            # if not root:
            #     return 0

            # q = deque()
            # if root:
            #     q.append(root)

            # level = 0
            # while q:
            #     for i in range(len(q)):
            #         node = q.popleft()
            #         if node.left:
            #             q.append(node.left)
            #         if node.right:
            #             q.append(node.right)
            #     level += 1
            # return level


            if not root:
                return 0
            
            return 1 + max(maxDepth(root.left), maxDepth(root.right))




        if not root: 
            return True

        left = maxDepth(root.left)
        right = maxDepth(root.right)

        if abs(left - right) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
 