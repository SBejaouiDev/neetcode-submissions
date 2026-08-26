class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        """
        Given an array nums, return the sum of all XOR totals for every subset of nums 

        
        """

        subset = []
        res = []
        total = 0
        def dfs(i,total): 
            print(total)

            if i == len(nums):
                return total

            return dfs(i + 1, total ^ nums[i]) + dfs(i + 1, total)
            """
            Python doesnt run this both calls at the same time. Finishes the left then completes the right
             think of this as 
             left = dfs(i + 1, total ^ nums[i])
             right = dfs(i + 1, total)
             return left + right
            """


        return dfs(0,total)
        print(res,total)
  

                