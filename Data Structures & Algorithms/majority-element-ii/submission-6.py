class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        Boyer-Moore Voting Algorithm
        ** would need to ask interviewee how many majority elements we are looking for to determine number of candidates
        1) Check for the majority elements  
        2) Then count the occurence of the elements 
        3) return candidates with count greater than n / 3 
        """
        n = len(nums)
        num1 = num2 = -1
        cnt1 = cnt2 = 0

        # determine the majority element
        for num in nums: 
            if num == num1: 
                cnt1 += 1
            elif num == num2:
                cnt2 += 1

            elif cnt1 == 0: 
                cnt1 = 1
                num1 = num 
            elif cnt2 == 0:
                cnt2 = 1
                num2 = num

            else: 
                cnt1 -= 1
                cnt2 -= 1

        ## count the occurence 
        cnt2 = cnt1 = 0
        for num in nums: 
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
        
        #count and return occurance list 
        res = []
        if cnt1 > len(nums) // 3: 
            res.append(num1)
        if cnt2 > len(nums) // 3 :
            res.append(num2)

        return res