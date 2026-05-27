from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suf = [1] * len(nums)
        pre = [1] * len(nums)
        output = []

        for i in range(1, len(nums)):
            print(pre[i-1], nums[i-1])
            pre[i] = pre[i-1] * nums[i-1]

        print(pre)

        for i in range(len(nums)-2,-1,-1):
            print(suf[i + 1], nums[i + 1])
            suf[i] = suf[i+1] * nums[i+1]

        print("Printing suffix",suf)

        for i in range(len(nums)):
            output.append(pre[i] * suf[i])

        return output

n = [1,2,4,6]
s = Solution()
print("Output", s.productExceptSelf(n))