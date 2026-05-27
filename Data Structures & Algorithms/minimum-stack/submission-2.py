class MinStack:


    def __init__(self, ):
        self.stack = []
        self.preStack = []


    def push(self, val: int) -> None:
        print("Running push")
        self.stack.append(val)
        self.preStack.append((val,min(self.stack)))

    #  removes the element on the top of the stack.
    def pop(self) -> None:
        # print("Running pop")
        # index = len(self.stack)
        # removedItem = self.stack[index]
        # del self.stack[index]
        # return removedItem
        self.stack.pop() ##built in python function
        self.preStack.pop()


    # gets the top element of the stack.
    def top(self) -> int:
        print("running top")
        index = len(self.stack)
        return self.stack[index - 1]

        #return self.stack.pop()

   # retrieves the minimum element in the stack.
    def getMin(self) -> int:
        index = len(self.preStack) - 1

        return self.preStack[index][1]





