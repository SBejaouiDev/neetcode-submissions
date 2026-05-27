class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        output = []


        
        while l < r:
            Sum = numbers[l] + numbers[r]
            if Sum == target and numbers[l] != numbers[r]:
                return output + [l+1, r+1]
            elif Sum <= target:
                #Since the values are in ascending order l ++ increase the sum value
                #print("sum greater than target increment l")
                l += 1
            else:
                # decreasing r decreases the sum value 
                #print("sum less than target increase L")
                r -= 1