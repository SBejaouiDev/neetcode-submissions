class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        """
        nums[i] + nums[j] = - nums[k]
        sort the array first
        """

        nums = sorted(nums)
        i = 0
        j = 0 
        res = []
    
        duplicate  = set()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]

            while j < k: 
                sum = nums[j] + nums[k]
                if sum == target:
                    res.append([nums[i],nums[j],nums[k]])
                    duplicate.add((nums[i],nums[j],nums[k]))
                    

    
                    k -= 1

                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                    #increment j

                elif nums[j] + nums[k] > -nums[i]:
                    #decrement k
                    k -= 1


        return list(duplicate)