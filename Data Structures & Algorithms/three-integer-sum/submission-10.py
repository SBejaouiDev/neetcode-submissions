
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        j = 0
        #k = len(nums) - 1
        nums.sort()

        duplicate = set()
        for i in range(len(nums)):

            j = i + 1
            k = len(nums) - 1

            target = -nums[i]
            while j < k:
                sum = nums[j] + nums[k]

                if nums[j] + nums[k] == target:

                    print(nums[i],nums[j],nums[k])
                    res.append([nums[i],nums[j],nums[k]])
                    #duplicate.append([nums[i],nums[j],nums[k]])
                    duplicate.add((nums[i],nums[j],nums[k]))
                    if sum < target:
                        j += 1
                    else:
                        k -= 1

                #increasing j since sum is less than target
                elif sum < target:
                    j += 1

                #decreasing j since sum is larger than target
                else:
                    k -= 1


        print(list(duplicate))
        return list(duplicate)

        #return res









s = Solution()
nums = [-1,0,1,2,-1,-4]
nums=[0,0,0,0]
nums=[-2,0,1,1,2]
print(s.threeSum(nums))