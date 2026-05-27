from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        r = 1

        maxP = 0

        while r < len(prices):
            # if prices[r] > prices[l] compute the profit

            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxP = max(maxP,profit)
            else:
                l = r
            r += 1

        return maxP














prices = [10, 1, 5, 6, 7, 1]
s = Solution()
print(s.maxProfit(prices))