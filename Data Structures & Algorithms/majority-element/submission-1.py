class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        - return the element that appears the most 5 1 5 5 retuns 5 
        - Majority element = element that appears more thant [n / 2] times in the array. (n is the size of the array)
        - Majority element always exisits 
        Input: nums array
        output: the majority element (int)

        use a hash to keep count of the items. The item that is appears n/2 more times in the array return
        time complexity bigO(n + m) two pass one for the count and the 2nd pass for the majority element return

        Optimize space to bigO(1) and linear time??
        treat the problem like a political election where different numbers elimate each other. 

        - count: the health of the candidate
        - candidate The number currently winning the battle
        """
        ## [7 / 2 times] the array]

        # majorityElement = {}

        # for i in nums:
        #     if i not in majorityElement:
        #         majorityElement[i] = 1
        #     else: 
        #         majorityElement[i] += 1

        # for key,value in majorityElement.items():
        #     if value > len(nums) / 2: 
        #         return key

        cand = 0
        count = 0 

        for num in nums: 
            if count == 0:
                cand = num
            
            if num == cand: 
                count += 1
            elif num != cand:
                count -= 1

        return cand

