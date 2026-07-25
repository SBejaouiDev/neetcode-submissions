class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                return mid
                
            # 1. Check if the RIGHT half is sorted first
            if nums[mid] <= nums[high]:
                # Target lies within the sorted right half boundaries
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
                    
            # 2. Otherwise, the LEFT half must be sorted
            else:
                # Target lies within the sorted left half boundaries
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
                    
        return -1