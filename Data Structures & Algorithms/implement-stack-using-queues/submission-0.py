class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        """
        push element x to the top of the stack
        P: 
        I: 
        """
        self.stack.append(x)
        print(self.stack)

    

    def pop(self) -> int:
        #self.stack.
       
        return self.stack.pop()

    def top(self) -> int:
        """
        Remove the element on the top of stack and return it
        Queue: first in first out 
        Stack: last in first out 
        """
        return self.stack[-1]


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