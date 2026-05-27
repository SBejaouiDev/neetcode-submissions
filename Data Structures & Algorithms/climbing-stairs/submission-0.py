class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = {}
        nums = [1,2]

        cache[0] = 1
        for i in range(1, n + 1):
            cache[i] = 0


            for num in nums:
                subproblem = i - num
                if subproblem < 0:
                    continue
                cache[i] = cache[i] + cache[subproblem]


        return cache[n]



        