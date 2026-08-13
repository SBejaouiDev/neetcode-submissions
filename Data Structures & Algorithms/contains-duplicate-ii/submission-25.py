class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dup = {}  # Stores value: index

        for i in range(len(nums)): 
            num = nums[i]
            #print(dup) 

            if num in dup:

                

                #print(abs(previous_index - i))
               #previous_index = dup[num]
               # if we come across a duplicate we check the prev and current index against k if its <= k return True
               # else we update the previous index to current index
                if abs(dup[num] - i) <= k:
                    return True
                #print(f"Found duplicate {num}. Current index: {i}, Previous index: {previous_index}")
                dup[num] = i
            else: 
                # First time seeing it, save it with its index
                dup[num] = i

        return False