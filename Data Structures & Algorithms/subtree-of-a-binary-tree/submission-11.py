# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        #DFS search algo 
        #toggle = False
        #stack = [root]

        # while stack: 
            
        #     q = stack.pop()
        #     print("Node",q.val)
        
        #     toggle = self.sameTree(q, subRoot)
        #     print("at node:", q.val,toggle)
        #     if q.right:
        #         stack.append(q.right)

        #     if q.left:
        #         stack.append(q.left)
        #     print("\n")

        #     if q.left and not q.right:
        #         print("incomplete tree")
        #         return False

        # if toggle:
        #     return True 

        # return True

        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        #if that node is not a subtree then move to next node

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot))



    def sameTree(self, treeOne: Optional[TreeNode], treeTwo: Optional[TreeNode]) -> bool:
        
        #both trees are null
        if not treeOne and not treeTwo:
            return True

        
        if treeOne and treeTwo and treeOne.val == treeTwo.val:
            #print(treeOne.val, treeTwo.val)
            return self.sameTree(treeOne.left, treeTwo.left) and self.sameTree(treeOne.right, treeTwo.right)
  
        
        return False

        

