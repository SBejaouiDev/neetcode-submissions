class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        topK = {}
        maxList = []

        for i in nums:
            topK[i] = topK.get(i, 0) + 1

        # print(topK )
        # print(max(topK, key = topK.get))
       
        while k != 0:
            maxValue = max(topK, key = topK.get)
            maxList.append(maxValue)
            del topK[maxValue]
            k -= 1

        return maxList