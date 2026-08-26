class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
        Given an array and an integer k. Return true f it is possible to divide this array into k non-empty subsets who sums are all equal

        [5], [2,3] ,[4,1] = 5 + 5 + 5
        
        Check to see if the sum divided by k is an int
        """

        total_length = sum(nums)

        # check if sum of array can be equally divided by k
        if sum(nums) % k != 0:
            return False

        length = total_length // k
        sides = [0] * k

        nums.sort(reverse=True)
        print(length,sides,nums,total_length) 

        def dfs(i):
            print(sides,i)

            #base case breaks the recursion
            if i == len(nums):
                return True

            for side in range(k):

                if sides[side] + nums[i] <= length:
                    sides[side] += nums[i]
                    
                    #after a number matches a side we move to the next number. 
                    if dfs(i + 1):
                        return True
                    
                    #back tracking part. 
                    sides[side] -= nums[i]

                if sides[side] == 0:
                    break

            return False    
            


        return dfs(0)
        