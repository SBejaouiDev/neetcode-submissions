from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

            ## group the together create stack
            pair = [(p,s) for p,s in zip(position,speed)]
            pair.sort(reverse=True)
            stack = []

            for p,s in pair:
                #calculate time it takes to teach target for each car
                stack.append(((target-p)/s))

                #if the new car time is less than or equal to the one before it
                # pop values that are in the same fleet. since cars cannot pass ahead
                # returns the number different car fleets
                if len(stack) >= 2 and stack[-1] <= stack[-2]:
                    stack.pop()


            return len(stack)


            print(stack)

            # for i in range(len(position)-1, -1,-1):
            #     print(speed[i])
            #
            #     distance = target - position[i]
            #     time = distance / speed[i]
            #
            #     print("distance for car", i, ":", distance, end=" ")
            #     print("time for car", i, ":", time)
            #
            #     if not stack:
            #         print("empty stack executed")
            #         stack.append(time)
            #
            #     if time <= stack[-1]:
            #         pass
            #         # stack.append((position[i],time)
            #     else:
            #         stack.append(time)





            # #sort array in descending order
            # for i,t in enumerate(position):
            #     distance = target - position[i]
            #     time = distance / speed[i]
            #     print("distance for car", i,":",distance, end = " ")
            #     print("time for car", i, ":", time)
            #
            #     if not stack:
            #         print("empty stack executed")
            #         stack.append(time)
            #
            #     if time > stack[-1]:
            #         #stack.append((position[i],time))
            #         stack.append(time)
            #
            #
            #     #count[time] = i
            #
            # print("printing stack", stack)
            #
            # return len(stack)


# target = 10
# position = [1,4]
# speed = [3,2]

target = 10
position = [4,1,0,7]
speed = [2,2,1,1]


s = Solution()
print(s.carFleet(target,position,speed))

