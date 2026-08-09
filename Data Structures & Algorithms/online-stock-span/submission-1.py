class StockSpanner:

    """ 
    Design an algo that collects daily price quotes for some stock and returns the span of that stocks price
    for the current day

    Span example: [7,2,1,2] stock price today: 2
    Span = 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days

    Plan: append each stock price to the stack. 
    
    We check todays price against past stocks by
        - popping elements from the stack that are less than or equal to todays price
        - for each pop increment the count.

    """
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        temp = []
        count = 0
        #print(self.stack)
        while self.stack and self.stack[-1] <= price:
            temp.append(self.stack.pop())
            count += 1 

        for item in reversed(temp):
            self.stack.append(item)
        
        #print(self.stack,count,"\n")
        
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)