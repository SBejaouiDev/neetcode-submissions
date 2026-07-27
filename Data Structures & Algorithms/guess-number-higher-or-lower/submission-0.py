# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        """
        use the given api to guess the correct number
        given a number from 1 to N. we guess
        l = 1 
        r = n 
        this is our search bound.
        if 0 we return mid
        if -1 decrease r 
        if 1 increase l 

        """
        l = 1
        r = n 
        while True: 
            print(l,r)
            mid = (l + r) // 2
            target = guess(mid)

            if target == 0:
                return mid
            elif target == -1: 
                r = mid - 1
            else:
                l = mid + 1