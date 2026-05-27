# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 


        #recursion appending the list after the for loop is done then the next iteration begins 
        def dfs(i,curr, total):

            if total == target: 
                res.append(curr.copy())
                return

            ## BaseCase 
            if i >= len(nums) or total > target:
                return

            curr.append(nums[i])
            dfs(i,curr, nums[i] + total)
            curr.pop() ## this means that we have exhausted all possible routes at nums[i]
            dfs(i+1, curr,total) ## we move to the next number

    

        dfs(0,[],0)
        return res