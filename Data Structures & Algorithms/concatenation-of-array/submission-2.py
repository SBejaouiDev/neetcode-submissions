class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        create an array that is 2n. Where n is the length of the array.
        [1,4,1,2] would be [1,4,1,2,1,4,1,2]
        
        create an array with size 2n 
        for each element in the array populate the new array by ans[1] and ans[1 + n]
        return the array
        """


        ans = (2 * len(nums))  * [0]
        print(ans)
        
        for i in range(len(nums)): 
            ans[i] = nums[i]
            ans[i + len(nums)] = nums[i]

        return ans

        # 0 4
        # 1 5 
        # 2 6 
        # 3 7