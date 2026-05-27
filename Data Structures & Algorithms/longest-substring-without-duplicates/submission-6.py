class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # fixed window size
        # increase window size when no matches are found
        # stop window size when match is found and return
        #window = {}
        window = []
        windowSize = 0
        start = 0

        l = 0
        r = 1

        maxSize = 0
        # for i in range(len(s)):
        #
        #     if s[i] not in window:
        #         print(i, s[i])
        #         window.append(s[i])
        #         print(f"Appended {s[i]}, new list: {window}")
        #         windowSize += 1
        #         maxSize = max(maxSize,windowSize)
        #
        #     else:
        #         windowSize = 0
        #         window.clear()
        #         #print(i,s[i])
        #         window.append(s[i])
        #         windowSize += 1
        #         print(f"Appended {s[i]}, new list: {window}")

        if len(s) == 0:
            return 0

        window.append(s[l])
        while r < len(s):
            #print("printing window", window)

            if s[r] not in window:
                window.append(s[r])

                maxSize = max(maxSize, len(window))

            else:
               # print("cleared window\n")
                window.clear()
                l += 1
                r = l

                #print("printing stored value at s[l]", s[l])
                window.append(s[l])

            r += 1

        maxSize = max(maxSize, len(window))
        #print(window)
        return maxSize


s = "zxyzxyz"
s = "xxxx"
# s="pwwkew"
# s="aab"
# s="dvdf"
s="zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"


window = Solution()
print(window.lengthOfLongestSubstring(s))