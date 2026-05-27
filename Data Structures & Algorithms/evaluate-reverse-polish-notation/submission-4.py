from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = ["*", "/", "+", "-"]
        #symbols = {"*": *, "/": 2, "+": 3, "-":4}
        numbers = []
        opList = []

        ## 3 4 + similar to
        sum = 0
        for i in range(len(tokens)):

            if tokens[i] not in symbols:
                numbers.append(int(tokens[i]))

            elif tokens[i] in symbols:

                if tokens[i] == "+":
                    topOfStack = numbers.pop()
                    bottomOfStack = numbers.pop()
                    sum = bottomOfStack + topOfStack
                    numbers.append(sum)
                    print("running")
                elif tokens[i] == "-":
                    topOfStack = numbers.pop()
                    print("inside elif of - ",numbers)
                    bottomOfStack = numbers.pop()
                    sum = bottomOfStack - topOfStack
                    numbers.append(sum)
                    print("running")
                elif tokens[i] == "/":
                    topOfStack = numbers.pop()
                    bottomOfStack = numbers.pop()
                    sum = int(bottomOfStack / topOfStack)
                    print(sum)
                    numbers.append(sum)
                    print("running")
                elif tokens[i] == "*":
                    topOfStack = numbers.pop()
                    bottomOfStack = numbers.pop()
                    sum = bottomOfStack * topOfStack
                    numbers.append(sum)
                    print("running")

            print("Printing numbers", numbers)
        return numbers.pop()



