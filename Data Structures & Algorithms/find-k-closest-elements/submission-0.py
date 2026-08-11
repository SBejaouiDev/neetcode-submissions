class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        given a sorted int array, two integers k and x, return the k closest integers to x in the array. 
        An int a is closer to x if an integer b if: 
        |a - x| < |b - x|
        |a - x| == |b - x| and a < b


        Input: arr = [2,4,5,8], k = 2, x = 6
        Output: [4,5]
        return the 2 closet integers to 6 in the array

        | 4 - 6 | < |  - 6 |

        """
                
        l = 0 
        r = len(arr) - k



        while l < r: 
            ## mid represents the left most part of window
            mid = (l + r) // 2
            print(l,r,mid)
            print((x - arr[mid]),(arr[mid + k] - x))
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else: 
                r = mid
        
        return arr[l:l+k]