class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        subset = []
        num = list(range(1,n+1))
        print("num array",num,len(num))


        def dfs(i):
            #print(subset)
            #base case
            if len(subset) == k and subset not in res:
                print("subset is length of k",subset)
                res.append(subset.copy())

            if i >= len(num):
                return 
                


                

            subset.append(num[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res