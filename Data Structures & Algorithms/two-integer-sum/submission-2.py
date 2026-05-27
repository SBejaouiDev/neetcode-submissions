class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSum = []
      
        sum = 0 
        j = 0
        for i in range(len(nums)):
            j = i
            while j+1 < len(nums):
                j += 1
                if nums[i] + nums[j] == target:
                    twoSum.append(i)
                    twoSum.append(j)

        return twoSum