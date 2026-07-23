class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        choose the weight capcity in each ship. We need the minimum capacity to carry all the weights in x amount of ships 
        [1,2,3,4,5] ships = 5

        What is the minimum weight capacity of a ship needed to deliver all weights in x amount of ships
        ship [1]
        ship [2]
        ship [3]
        ship [4]
        ship [5]

        - Binary search problem within the bounds of [maxWeight, sumOfWeight] 
        set the search range [maxWeight, sumOfWeight] 
             l = maxWeight
             r = sumOfWeights
        
        while the l <= right
            mid is the current capcity to test

            for each capacity we test the amount of ships that can hold.
                - we create a seperate function to keep track of this. we iterate through the weights. if the capacity - the weight[i] 
                    is less than 0. we will need another ship so we increment ship. If the ship count is past the amount of ships we have return false. 
                    otherwise we decrease the capacity for the current ship. If we have went through each weight successfully we return True

            if the capacity can ship we set r = mid - 1 and we set res to the min capacity between the capacity we just tested and currentCapcity

            if the capacity can not ship. We set l = mid + 1, increasing our capacity a ship can hold
            
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