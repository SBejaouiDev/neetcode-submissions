# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0

        # depth = 0 

        # stack = [root]
        # #visited = []
        # maX = 0
        # while stack: 

        #     s = stack.pop()
        #     depth += 1
        #     if depth > maX:
        #         maX = depth
        #     if s.left: 
        #         stack.append(s.left)
        #     if s.right: 
        #         stack.append(s.right)

        # return maX


        queue = deque([root])
        depth = 0
        while queue: 
            levelSize = len(queue)

            for i in range(levelSize):
                s = queue.popleft()

                if s.left:
                    queue.append(s.left)
                if s.right:
                    queue.append(s.right)
            depth += 1



        return depth 
