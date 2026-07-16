class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
    
        nums = sorted(nums)
        print(nums)
        def dfs(i): 
            if subset in res:
                return            
            
            if i >= len(nums):
                res.append(subset.copy())
                return


            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
            # BASE CASE



        dfs(0)
        return res