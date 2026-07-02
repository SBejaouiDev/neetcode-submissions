class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: 
            return [[]]

        print(nums[1:])

        perms = self.permute(nums[1:])
        res = []

        for perm in perms: 
            print(len(perms))
            for i in range(len(perm) + 1): ##plus one because the len of the array is 0 since the list is empty []

                p_copy = perm.copy()
                p_copy.insert(i,nums[0])
                res.append(p_copy)
            
        return res


        
