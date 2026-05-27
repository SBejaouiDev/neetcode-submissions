from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        sort = sorted(nums)
        print(sort)
        sortDic = defaultdict(list)

        sortD = {}

        for i in sort:
            sortD[i] = sortD.get(i,0) + 1

        newList = list(sortD.keys())
        print("Printing the new list", newList)

        j = 0
        counting = 1
        count = 1

        for i in range(1, len(newList)):
            if newList[i] - newList[j] == 1:
                print("subtracting", newList[i], "-", newList[j], "=", newList[i] - newList[j])
                counting += 1
            else:
                counting = 1

            if counting > count:
                count = counting

            j += 1

        return count


nums = [2,20,4,10,3,4,5]
#nums = [-1, -1, 0, 1, 3, 4, 5, 6, 7, 8, 9]
s = Solution()
print(s.longestConsecutive(nums))



