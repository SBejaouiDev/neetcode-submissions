class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        # memo = [[-1] * 2 for _ in range(len(nums))]
        memo = [None] * len(nums)
        for i in range(len(nums)):
            memo[i] = [-1,-1]

        print(memo)
    
        # bottom up or top down? 
        # Top down 

        def dfs(i, flag):
            print("Running DFS")

            #base case 
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0

            if memo[i][flag] != -1:
                return memo[i][flag]
            
            #decision process rob or skip 
            memo[i][flag] = max(nums[i] + dfs(i + 2,flag), dfs(i + 1,flag))
    
        
            return memo[i][flag]


        return max(dfs(0, True), dfs(1,False))



        
        