class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        - return the element that appears the most 5 1 5 5 retuns 5 
        - Majority element = element that appears more thant [n / 2] times in the array. (n is the size of the array)
        - Majority element always exisits 
        Input: nums array
        output: the majority element (int)

        use a hash to keep count of the items. The item that is appears n/2 more times in the array return
        """
        ## [7 / 2 times in the array]



        majorityElement = {}

        for i in nums:
            if i not in majorityElement:
                majorityElement[i] = 1
            else: 
                majorityElement[i] += 1


        for key,value in majorityElement.items():
            if value > len(nums) / 2: 
                return key


