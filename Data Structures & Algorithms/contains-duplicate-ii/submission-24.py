class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dup = {}  # Stores value: index

        for i in range(len(nums)): 
            num = nums[i]
            #print(dup) 

            if num in dup:

                # SUCCESS: We found a duplicate! 
                # You can now access its previous index directly using the dictionary key:
                previous_index = dup[num]
                #print(abs(previous_index - i))
                if abs(previous_index - i) <= k:
                    return True
                #print(f"Found duplicate {num}. Current index: {i}, Previous index: {previous_index}")
                dup[num] = i
            else: 
                # First time seeing it, save it with its index
                dup[num] = i

        return False