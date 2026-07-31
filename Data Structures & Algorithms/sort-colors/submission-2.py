class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        How can we bounds? 

        """
        l = 0
        r = len(nums) - 1

        i = 0
        while i <= r: 
            #print("L:",l,"i:",i,"r:",r,nums)
            if nums[i] == 2: 
                #swap 
                temp = nums[i]
                nums[i] = nums[r]
                nums[r] = temp
                r -= 1
                i -= 1
                #we cannot move to the next element because we have to make sure the element we swapped is in the correct
                #order. 

            
            elif nums[i] == 0: 
                temp = nums[i]
                nums[i] = nums[l]
                nums[l] = temp
                l += 1
            
            i +=  1
