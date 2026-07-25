class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1 
        
        """
        Identify the sorted side
                ↓
        Check whether target is inside that sorted side
                ↓
        If yes, search it
        If no, search the other side
        """

        while l <= r:
        # find pivot 
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
        
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
  

        return -1