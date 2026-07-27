class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l = 0 
        r = len(nums) - 1

        """ 
        Preform binary search on the array. If the target is not found we return the index of where it should go

        With binary search we incease L if the target is greater than the middle value and reduce the right 
        index if the target is less than the nums[middle]. 
        - If the target is not found the middle point tells us where the value should be
        if the target is greater than the middle point it needs to be placed mid + 1. if the target is less than it should be placed 
        where the middle is currently located. 
               l r  
        [1,3,5,7,9] target = 6
               m

        target < 7 so the index would be 3
        """
        
        while l <= r: 
            mid = (l + r) // 2
            print(l,r,mid)

            if nums[mid] == target:
                return mid

            elif target > nums[mid]:
                l = mid + 1
                
            else:
                r = mid - 1 
        return l
        print(l,r,mid)
        if target > nums[mid]:
            return mid + 1
        else:
            print("running")
            return mid 


