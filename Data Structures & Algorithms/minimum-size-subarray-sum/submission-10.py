class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """


        """
        i = 0 
        j = 0
        s = 0 
        minLength = 100001
        while i <= len(nums) -1: 
            print(i,j)
            if s < target and j < len(nums):

                #grow the window
                s += nums[j]
                j += 1

            elif s >= target: 
                 minLength = min(minLength, len(nums[i:j]))
                 s -= nums[i]
                 i +=1 
            else:
                break

        if minLength == 100001: 
            return 0
        else:
            return minLength
        
