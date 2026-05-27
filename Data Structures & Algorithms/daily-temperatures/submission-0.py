from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        monStack = [] #[temp,index]
        result = [0] * len(temperatures)

        for i,t in enumerate(temperatures):

            while monStack and monStack[-1][1] < t:
                print("\n")
                print("The index at monStack", monStack[-1][1])

                index = monStack.pop()
                result[index[0]] = (i - index[0])

            print("appending", i,t)
            monStack.append((i,t))

        return result



temperatures = [30,38,30,36,35,40,28]

s = Solution()
print(s.dailyTemperatures(temperatures))