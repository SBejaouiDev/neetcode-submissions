class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for asteroid in asteroids:
            #compare sizes if the astriod is - and the top of res is positive. Collision
            while res and (asteroid < 0) and (res[-1] > 0):  
                #print(asteroids, res)
                diff = asteroid + res[-1]
            
                if diff < 0:
                    res.pop()
                
                #if the top is larger discard current
                elif diff > 0:
                    asteroid = 0

                #if the nodes are equal 
                else: 
                    #print("executing here")
                    asteroid = 0
                    res.pop()

            if asteroid:
                res.append(asteroid)
                
        return res