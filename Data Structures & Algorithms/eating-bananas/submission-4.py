from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        M = max(piles) ## why are we doing this.
        l = 1
        r = M
        res = r


        while l <= r:
            mid = (l + r) // 2 ## this is our k
            hour = 0

            for x in range(len(piles)):
                hour += ceil(piles[x]/mid) ## this is our hours to compare with H

            if hour > h:
                l = mid + 1

            else:
                res = mid
                r = mid - 1

        return res







s = Solution()
piles = [1,4,3,2]
h = 9
print(s.minEatingSpeed(piles,h))