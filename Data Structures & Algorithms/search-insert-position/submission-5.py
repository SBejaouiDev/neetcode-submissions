class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l = 0 
        r = len(nums) - 1

        while l <= r: 
            mid = (l + r) // 2
            print(l,r,mid)

            if nums[mid] == target:
                return mid

            elif target > nums[mid]:
                l = mid + 1
                
            else:
                r = mid - 1 


       
        #return mid + 1
        if target > nums[mid]:
            return mid + 1
        else:
            return mid 
            print("not found")

        print(l,r) 
        return 0