class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ## O(N) complexity
        # nums.sort()
        # print(nums)
        # return nums[len(nums) - k]



        ## using maxHeap 

        heapq.heapify(nums)
        print(nums)

        while len(nums) >= k + 1:
            heapq.heappop(nums)


        print(nums)
        return nums[0]
