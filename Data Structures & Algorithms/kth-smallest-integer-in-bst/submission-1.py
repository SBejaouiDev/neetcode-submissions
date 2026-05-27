# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        

        array = [] 

        q = deque([root])


        while q: 
  
            for i in range(len(q)):
                node = q.popleft()
                array.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right: 
                    q.append(node.right)

            

        array.sort()
        print(array)

        return array[k-1]

        return 1