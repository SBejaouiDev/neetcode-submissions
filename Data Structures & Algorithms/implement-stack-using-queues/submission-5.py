class MyStack:

    def __init__(self):
        self.stack = deque()
        self.queue2 = deque()
    def push(self, x: int) -> None:
        """
        push element x to the top of the stack
        P: To create a stack using queues. We append the item we are pushing to the 2nd queue. 
        then we traverse and popleft each element from the first queue and append it to the 2nd queue. 
        queue = [1,2,3] push 4 

        queue2 = [4]
               = [4,1,2,3]
        I: 
        """
        # self.queue2.append(x)
        # while self.stack:
        #     self.queue2.append(self.stack.popleft())
        
        # #dont understand this. Pythonic way of doing a swap
        # #self.stack, self.queue2  = self.queue2, self.stack

        # temp = self.stack 
        # print("stack", temp )
        # self.stack = self.queue2 
        # self.queue2 = temp 

        ## how would you optimize this and use one queue? 
        self.stack.append(x)
        for items in range(len(self.stack) - 1):
            self.stack.append(self.stack.popleft())

    def pop(self) -> int:
        #self.stack.
        """
        remove top element from stack and return it
        queue: 5 4 3 2 1 
        stack: 1 2 3 4 5
        To remove top element from stack we need to pop from the left side of the queue. 
        """
        return self.stack.popleft()

    def top(self) -> int:
        """
        Remove the element on the top of stack and return it
        Queue: first in first out 
        Stack: last in first out
        queue = 5 4 3 2 1 
        stack = 1 2 3 4 5 
        the fist item in the stack needs to looked at. 
        This is equalivant to looking at the first element in a queue
        """
        return self.stack[0]


    def empty(self) -> bool:
        if len(self.stack) != 0:
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()