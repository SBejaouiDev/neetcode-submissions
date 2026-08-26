class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, subset):
            print(subset)  

            ## creates the subset
            for j in range(i, len(nums)):
                subset.append(nums[j])
                backtrack(j + 1, subset)
                res.append(subset.copy())
                subset.pop()

                
        backtrack(0, [])
        res.append([])
        return res
