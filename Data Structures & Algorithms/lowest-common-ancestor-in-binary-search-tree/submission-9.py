# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:


        ##DFS queue 

        queue = deque([root])
        print(p.val,"q")
        print(q.val,"q\n")


        if not root:
            return node

        while queue: 

            for i in range(len(queue)):
                node = queue.popleft()
                print(node.val)

                if p.val <= node.val <= q.val or p.val >= node.val >= q.val: 
                    print("split has occured")
                    if node.left: 
                        queue.append(node.left)
                    if node.right: 
                        queue.append(node.right)
                    return node

                elif p.val > node.val:
                    print("curr node", node.val, "going right subtree")
                    if node.right: 
                        queue.append(node.right)


                elif q.val < node.val:
                    print("curr node", node.val, "going left subtree")
                    if node.left: 
                        queue.append(node.left)





            #print("new level\n")
        return root



        