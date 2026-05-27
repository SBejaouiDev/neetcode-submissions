from typing import List
import math


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        targetRow = 0
        l = 0
        #h = len(matrix) - 1
        colLen = len(matrix[0]) - 1



        rowTarget = 0
        ## find the row that the target is in
        for i in range(len(matrix)):
            print(matrix[i][0],matrix[i][colLen])
            if matrix[i][0] <= target <= matrix[i][colLen]:

                while l <= colLen:
                    mid = math.floor( (l + colLen) / 2 )
                    print("mid", mid)
                    if target == matrix[i][mid]:
                        return True

                    elif target < matrix[i][mid]:
                        colLen = mid - 1
                    elif target > matrix[i][mid]:
                        l = mid + 1

        return False



m = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]

#m = [[1,3]]

matrix = Solution()

print(matrix.searchMatrix(m, 10))







