class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        Find elements that appear more than n/3 times. 
        n = array size 
        num = array of numbers 

        [10/3] = find elements that appear more than 3.33 times
        2 appears 5 times
        5 appears 4 times

        How to solve problem in linear time and space? 

        We can treat it like a debate. 
        """
        numDict= {}
        res = set()

        for i in nums: 
            if i not in numDict:
                numDict[i] = 1
            else:
                numDict[i] += 1
            
            if numDict[i] > (len(nums) / 3):
                res.add(i)
        
        return list(res)



        