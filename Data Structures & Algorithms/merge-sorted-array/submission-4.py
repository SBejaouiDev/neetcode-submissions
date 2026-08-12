class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        Input: Two arrays, two integers.
            - m valid elements in num1 
            - n number of elements in num2

        merge the two arrays such that the final merged array is in increasing order and stored within nums 1.
        num1 length = m + n 

        three pointers. 
            - i tracks the last VALID ELEMENT IN nums1  
            - j tracks the last element in num2
            - k tracks the very last element in nums1

        The trick is is to append from the end instead of the front.
        1) compare numbers at nums1[i] and nums2[j].
        2) the larger number is appended to the position at k. 
        3) decrement k and the larger pointer(i or j)
        5) repeat until we are done checking one of the arrays

        if nums1 runs out of elements first, copy the rest of the elements from nums2 to the front of nums1.
        If nums2 runs out of elements we are done since the remaining elements are already in their correct position

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

        while j >= 0: 
            nums1[k] = nums2[j]
            j -= 1
            k -=1

        
         