class Solution:
    def mySqrt(self, x: int) -> int:
        ## babylonian method 
        r = x

        while r * r > x: 
            ## or it can be divided by two
            r = (r + x // r) // 2
            print(r)

        return r