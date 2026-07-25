class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1 
        
        """
        Linear shrinking. If we have duplicate values we wont be able to tell what side is sorted or 
        whether the rotation point is hidden behind values. We shrink the search boundaries by one. 

        We can safely do this because we checked if the mid is the target, since 
        nums[r] == nums[mid] == nums[l]. we can disgard those values. 

        1) is nums[mid] == target
        2) are nnums[r] == nums[mid] == nums[l]
            - Remove duplicate values
        3) determine which side is normally sorted
        4) Check whether the target lies in that sorted side.
        https://chatgpt.com/share/6a642d9a-bf4c-83e8-ae43-efef69ef5fe2

        """
        while l <= r:
        # find pivot 
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return True

            if nums[mid] == nums[r] == nums[l]:
                print(nums[l],nums[mid], nums[r] )

                l += 1
                r -= 1
                continue

            ## check if the right is normally sorted
            if nums[mid] <= nums[r]:
                print("right normally sorted")

                ##target is inside the right side
                if nums[mid] < target <= nums[r]:
                    l = mid + 1

                else: 
                    r = mid - 1

            #other wise left must be sorted
            else:

                # target is inside the left side?
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  

                # target is in the right half
                else: 
                    l = mid + 1 
  

        return False 