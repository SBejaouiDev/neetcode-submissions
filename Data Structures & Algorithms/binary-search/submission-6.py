class Solution:
    def search(self, nums: List[int], target: int) -> int:

        
        low = 0
        high = len(nums) 

        while low <= high:

            mid = math.floor((low + high) / 2) 
            if nums[mid] == target: 
                return mid
            elif target < nums[mid]: 
                #eliminate upper half: set H to left of MIDDLE INDEX
                high = mid - 1
            else: 
                #eliminate lower half: Set low to right of MIDDLE index
                low = mid + 1 

            
        
        return -1 
            