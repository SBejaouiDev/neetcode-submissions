from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = nums[0]
        l = 0
        h  = len(nums) - 1


        while l <= h:
            mid = (l + h) // 2
            if target == nums[mid]:
                return mid
            #print("L:",l, "M:",mid, "r:",h)
            #print("search value",nums[mid], "\n")

            # if nums[mid] < target < nums[h]:
            #     if target == nums[mid]:
            #         return nums[mid]
            #     elif target >= nums[mid]:
            #         l = mid + 1
            #     else:
            #         h = mid - 1
            # else:
            #     if target == nums[mid]:
            #         return nums[mid]
            #     elif target >= nums[mid]:
            #         l = mid + 1
            #     else:
            #         h = mid - 1


            ## lies in the right part
            if nums[l] <= nums[mid] :
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    h = mid - 1


            ## lies in the left part
            else :
                if target < nums[mid] or target > nums[h]:
                     h = mid - 1
                else:
                     l = mid + 1

        return -1







nums = [3,4,5,6,1,2]
target = 3

# nums1=[3,5,6,0,1,2]
# target1=4

# nums=[4,5,6,7,0,1,2]
# target=0

s = Solution()
print(s.search(nums,target))



