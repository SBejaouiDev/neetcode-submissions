class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    
        seen = set()
        toggle = False

        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)

        return toggle   