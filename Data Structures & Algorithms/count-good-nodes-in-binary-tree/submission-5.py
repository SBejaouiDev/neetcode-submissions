# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:



        output = []
        #queue = deque( [(root,0)] )
        queue = deque()
        queue.append( (root,-float('inf')) )

        res = 0

        while queue:
                node,maxval = queue.popleft()    
                  

                if node.val >= maxval:
                    res += 1

                if node.left:
                    queue.append( (node.left,max(maxval,node.val)) )
                
                if node.right:
                     queue.append( (node.right,max(maxval,node.val)) )


                
        
        return res 
        