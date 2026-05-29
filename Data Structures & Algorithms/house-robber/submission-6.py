class Solution:
    def rob(self, nums: List[int]) -> int:
        


        #skip
        #rob 

        #stores max money from house
        memo = [-1] * len(nums)



        def dfs(i): 
            print("working")

            #if out of bounds return 0
            if i >= len(nums):
                return 0
            
            #if memo is already computed return it
            if memo[i] != -1:
                return memo[i]


            #               skip        rob
            memo[i] = max(dfs(i + 1), dfs(i+2) + nums[i])
            return memo[i]



     


        return dfs(0)