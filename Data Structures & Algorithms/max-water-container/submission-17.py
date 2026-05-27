class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max = 0
        area = 0

        while l <= r:

            distance = r - l
            print("left:",l, "right:",r, "Max value:",max)

            # left side larger than right
            if heights[l] > heights[r]:
                area = heights[r] * distance
                r -= 1

            # right side is larger than left
            elif heights[l] < heights[r]:
                area = heights[l] * distance
                l += 1


            #equal distance
            else:
                area = heights[l] * distance
                l += 1

            # max
            if area > max:
                max = area

        return max