# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        ##base case 
        """"
        we know the rootNode is the first element in preOrder array.
        We look for that index in the inOrder array. 

        """
        self.currentIndexPre = 0   
        #create a hash for inorder array for O(1) look up
        val_to_index = {val:idx for idx, val in enumerate(inorder)}
        print(preorder,inorder)

        
        def dfs(l,r):
            if l > r:
                return None
            
            root_val = preorder[self.currentIndexPre] # For each node in preorder array find index in the in-order array 
            self.currentIndexPre +=1 # increment the global index 
            root = TreeNode(root_val) # create a newNode for each iteration 
            
            ##Where the split occurs
            mid = val_to_index[root_val] 

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root


        return dfs(0,len(inorder)- 1)
        