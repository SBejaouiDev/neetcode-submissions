import math
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        #nums.sort()
        res = nums[0]
        l = 0
        h  = len(nums) - 1
        print(nums)

        while l <= h:
            # min will be on one of the groupings

            ## array is already sorted
            if nums[l] < nums[h]:
                res = min(res, nums[l])
                break


            mid = math.floor((l + h) / 2)
            res = min(res, nums[mid])
            
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                h = mid - 1

        return res








S = Solution()
nums = [3,4,5,6,1,2]
print(S.findMin(nums))