class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # my solution
        # fixed window size
        # increase window size when no matches are found
        # stop window size when match is found and return
        # window = []
        #
        # l = 0
        # r = 1
        #
        # if len(s) == 0:
        #     return 0
        #
        # window.append(s[l])
        # while r < len(s):
        #
        #     if s[r] not in window:
        #         window.append(s[r])
        #         maxSize = max(maxSize, len(window))
        #     else:
        #         window.clear()
        #         l += 1
        #         r = l
        #         window.append(s[l])
        #
        #     r += 1
        #
        # maxSize = max(maxSize, len(window))
        # return maxSize


        ## sliding window
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            res = max(res, r-l + 1)

        return res




s = "zxyzxyz"
s = "xxxx"
# s="pwwkew"
# s="aab"
# s="dvdf"
s="zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"


window = Solution()
print(window.lengthOfLongestSubstring(s))