# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []

        ##DFS and append all the nodes in the level
        ##pop the first elemetn from each level append to a list 
        ## return the list

        queue = deque([root])
        layerNodes = []
        while queue: 
            temp_list = []
            for i in range(len(queue)): 
                node = queue.popleft()
                temp_list.append(node.val)
                if node.left: 
                    queue.append(node.left)
                if node.right: 
                   queue.append(node.right)
            layerNodes.append(temp_list)
    
        output = []
        for i in layerNodes:
            output.append(i.pop())
            





        return output



        