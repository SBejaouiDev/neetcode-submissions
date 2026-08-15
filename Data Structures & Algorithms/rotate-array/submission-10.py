class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        We can use a threestep reversal algoirthm. We define a help function called reverse that reverses the array.
        We then call that function 3 times.

        1) reverses the whole array 
        2) reverse the array from start to k - 1
        3) reverse the array from k to length of array
        if k is greater than the length of array we can use modules to find how many rotations. 
        k = 8 len(array) = 4 
        after modules k = 4. 

        example [1, 2, 3, 4, 5, 6, 7, 8] k = 4
            1st - 8 7 6 5 4 3 2 1
            2nd - 5 6 7 8 4 3 2 1
            3rd -  5 6 7 8 1 2 3 4 

        edge cases if k is greater than the length. 
        k % N. 

        why k % n works: 

        modules works because diving k by n removes the full cycles. The remainder tells us the exact spot you land on
        after you finish those cycles
        """
        
        
        #if k > len(nums) -1:
        if k == len(nums) or k == 0:
            return 

        print( k % len(nums) -1)

        if k > len(nums):
            k %= len(nums)


        
        

        #verse the the whole array
        self.reverse(nums,0,len(nums)-1)

        #reverse the first half of the elements
        self.reverse(nums,0,k - 1)

        #reverse the second half of the elements 
        self.reverse(nums,k, len(nums)-1)

        print(nums)


    def reverse(self,nums,start,end):
        print(nums,start,end)
        while start < end: 
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1        