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
        we know the rootNode of the tree is the first element in preOrder array.
        We can find where the tree splits by locating where the rootNode from preorder is located in the inorder array

        For faster lookup convert the inrder array into a hash. Using (key:Value, value: index)
        A DFS can be used to build a tree. 
        - For each node in pre-order we find the index in the inorder array. Create a new TreeNode and increment the global index.
        - Locate where the split happens by searching through the hashmap 
        - use l and r to keep track of the positions in inOrder array
        - recurisvely call dfs 
             for left node from l to mid - 1 
             for right node from r to mid + 1

        The run time is bigO(n) since we have to iterate through every element in preOrder
        space would also be big0(n)
        """
        self.currentIndexPre = 0   
        # create a hash for inorder array for O(1) look up
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
        