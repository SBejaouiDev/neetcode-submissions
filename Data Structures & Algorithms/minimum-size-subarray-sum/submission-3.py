class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Find the MINIMAL length of a subaray whose sum is greater than or equal to the target. 
        if no such subarray return 0
        input: target: positive int, nums: array
        output: length of subarray(int)

        Example:[2,1,5,1,5,3] , target = 10 
        Output: 3 
        why?    [5, 1, 5] because 5 + 1 + 5 = 11

        Plan: using a dynamic sliding window. 

        if windows values do not add up grow the window to the right. 
        - add to the sum
        - increment the right pointer

        if the windows value add up more than target shrink the window from left. 
        - find the minLength of subarray 
        decrease the sum
        and increment left pointer

        """

        sum = 0
        left = 0 
        right = 0
        minLenth = 100001

        while left < len(nums) -1: 
            print("Current sum",sum)

            if(sum < target and right < len(nums)):

                # grow the subarray by expanding right window   
                sum += nums[right]
                right += 1

            elif (sum >= target):
                ## find the min length of subArray
                minLenth = min(minLenth, right - left)
                sum -= nums[left]
                left += 1

            else:
                break
  
        if minLenth == 100001:
            return 0
        else:
            return minLenth

