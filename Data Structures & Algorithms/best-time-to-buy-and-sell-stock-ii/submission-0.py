class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ## Memorization (use recursion to break down problem into smaller sub problems ) 


        ## Bottom up tabulation. Iterative approach 

        profit = 0

        for today in range(1,len(prices)): 
           
            if prices[today] > prices[today - 1]:
                profit += (prices[today] - prices[today - 1])

        return profit