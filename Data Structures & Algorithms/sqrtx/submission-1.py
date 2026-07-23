class Solution:
    def mySqrt(self, x: int) -> int:
        ## babylonian method 
        r = x

        while r * r > x: 
            r = (r + x // r) // 2
            print(r)

        return r