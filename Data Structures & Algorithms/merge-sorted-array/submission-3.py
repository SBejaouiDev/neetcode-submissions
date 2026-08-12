class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        Input: Two arrays, two integers.
            - m valid elements in num1 
            - n number of elements in num2

        merge the two arrays such that the final merged array is in increasing order and stored within nums 1.
        num1 length = m + n 


        """
        
        i = m - 1 ##tracks last element in num1

        j = n - 1 ##tracks last element in num2

        k = (m + n) - 1 ##tracks last elements nums1 

        res = []
        #print(nums1[4:6] + nums1[:4])
        while j >= 0 and i >= 0:
            #print(nums1[k],nums2[j])
            #print(nums1[i])

            # nums1larger 
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1

            else: #nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        #print("nums1:",nums1, print(k))
        while j >= 0: 
            nums1[k] = nums2[j]
            j -= 1
            k -=1

        
         