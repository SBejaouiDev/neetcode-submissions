class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        ##sort the array 
        candidates.sort()

        def dfs(i,currentList, total):
            

            if total == target:
                res.append(currentList.copy())
                return 

            # base case to exist out of loop
            if i == len(candidates) or total > target:
                return

            currentList.append(candidates[i])
            dfs(i+1,currentList, candidates[i] + total)
            currentList.pop()


            #don't understand. This is skipping the duplicate value. 
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            #exclude current number
            dfs(i+1,currentList,total)


        dfs(0,[],0)
        return res
        