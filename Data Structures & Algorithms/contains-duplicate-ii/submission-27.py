class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dup = {}  # Stores value: index
        """     
        Determine if the duplicate value is within length of k. 

        Plan: 

        Use hash to store the index for each number. 
        iterate through the array, and check for duplicates.
        If we come across a duplicate check if previous index and the current index <= k. If it is return True
        else update the previous index to current index.
        bigO(n)
        """
        for i in range(len(nums)): 
            num = nums[i]

            if num in dup and abs(dup[num] - i) <=k:
               # print(f"Found duplicate {num}. Current index: {i}, Previous index: {previous_index}")

               # if we come across a duplicate we check the prev and current index against k if its <= k return True
               # else we update the previous index to current index
                #if abs(dup[num] - i) <= k:
                    return True
                # First time seeing it, save it with its index
            dup[num] = i

        return False