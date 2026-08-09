class StockSpanner:

    """ 
    Design an algo that collects daily price quotes for some stock and returns the span of that stocks price
    for the current day

    Span example: [7,2,1,2] stock price today: 2
    Span = 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive days

    Plan: append each stock price to the stack. 
    
    We check todays price against past stocks by
        - popping elements from the stack that are less than or equal to todays price
        - each popped element is append to an array to append back to the list
        - for each pop: increment the count.
        


    How can this be optimized?  our old approach keeps scanning the same elements. We can use a 
        - Montonic decreasing stack: A stack that remains in decreasing order.

        in the stack = [price,count]
        when a new price arrives we pop all entries that are less than or equal to todays price, 
        The popped entries represent consecutive days that are now covered by the current higher price
        - Allows us not to repeadedly scan all the items since the popped elements are stored at the current higher price

    """
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        print(self.stack)
        count = 1
        #print(self.stack)
        while self.stack and self.stack[-1][0] <= price:
            count += self.stack[-1][1]
            self.stack.pop() 
    
        self.stack.append((price, count))
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)