# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

       #BFS approach queue 

        pOne = deque([p])
        qTwo = deque([q])
    

        while pOne and qTwo: 
          
            for i in range(len(pOne)):
                treeOne = pOne.popleft()
                treeTwo = qTwo.popleft()
               

                if treeOne is None and treeTwo is None:
                    continue 
                
                #print("comparing", treeOne.val, treeTwo.val)
                if treeOne is None or treeTwo is None or treeOne.val != treeTwo.val:
                    return False

   
                pOne.append(treeOne.left)
                pOne.append(treeOne.right)
                qTwo.append(treeTwo.left) 
                qTwo.append(treeTwo.right)
            

        return True