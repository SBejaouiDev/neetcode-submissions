class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        total_length = sum(matchsticks)

        #Calculate the total length. If not divisible by 4, return false immediately.
        if sum(matchsticks) % 4 != 0:
            return False

        length = total_length // 4
        sides = [0] * 4
        matchsticks.sort(reverse=True)

        def dfs(i): 
            #print(i, sides)

            #basecase.
            if i == len(matchsticks):
                return True

            # for each side 
            for side in range(4):

                # if the matchstick is equal to or less than a length of a side add it to a side
                if sides[side] + matchsticks[i] <= length:
                    sides[side] += matchsticks[i]
                    
                    if dfs(i + 1):
                        return True

                    sides[side] -= matchsticks[i]
                
                if sides[side] == 0:
                    break 

            return False

        return dfs(0)

        # dfs(0) → where can I put 4?
        # dfs(1) → where can I put 4?
        # dfs(2) → where can I put 3?
        # dfs(3) → where can I put 2?
        # dfs(4) → where can I put 2?
        # dfs(5) → where can I put 1?


           