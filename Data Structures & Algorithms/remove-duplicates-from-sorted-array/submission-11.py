class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0 

        """ 
        Fast and slow pointer. 

        When a unique element is found we increase the slow pointer 
        and copy the value from the fast pointer to nums[slow]. 
        Otherwise we continue.

        we are moving all unique elements to the front. 
        Slow + 1 is the amount of unique elements, since only increment i when unique element is found
        """

        for j in range(1,len(nums)):
            
            #unique element found
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            print(nums)
            
        print(nums[:3])
        print(i + 1)
        return i + 1