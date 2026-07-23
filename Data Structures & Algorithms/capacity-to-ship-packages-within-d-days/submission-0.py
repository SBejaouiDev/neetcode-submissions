class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        choose the weight capcity such that it is the minimal capcity that we need to carry all the weights in x amount of ships 

        - Binary search problem within the bounds of [maxWeight, sumOfWeight] 
        set the search range [maxWeight, sumOfWeight] 
             l = maxWeight
             r = sumOfWeights
        
        while the l <= right
            mid is the current capcity to test
            
        """


        l = max(weights)
        r = sum(weights)
        res = r #set to the highest bound

        print(l,r)
        def canShip(mid):
            ship = 1
            cap = mid
            for w in weights: 
                if cap - w < 0:
                    ship += 1
                    if ship > days:
                        return False
                    cap = mid
    
                cap -= w
            return True

        while l <= r: 
            mid = (l + r) // 2 
 
            if canShip(mid):
                res = min(res,mid)
                r = mid - 1
            else:
                l = mid + 1

        return res