class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        Given people where people[i] is the weight of the ith person and an infinte number of boards that carrys a max 
        weight of limit.  

        - Each boat carries at most two people at the same time. 
        - The sum of the weight of those people is at most limit

        Return the min number of boats to carry every given person

        Example: people = [5,1,4,2], limit = 6
        [5,1]
        [4,2]
        Output: 2 

        [1,3,2,3,2], limit = 3
        [3]
        [3]
        [1,2]
        [2]
        output 2

        Sort the array
        Use two pointers. 
        One tracking the lightest person and the other tracking the heaviest person
        """

        l = 0  
        r = len(people) -1
        boats = []
        people = sorted(people)

        while l <= r: 
            #print(boats,people[l],people[r])
            #boat = []
            s = people[l] + people[r]

            if(s == limit or s <= limit):
                boats.append([people[l],people[r]]) 
                l += 1
                r -= 1

            elif people[r] <= limit:
                boats.append(people[r])
                r -= 1

            elif people[l] <= limit:
                boats.append(people[r])
                l += 1
            
            elif s > limit:
                r -= 1
            
            elif s < limit:
                l += 1
            #boats.append(boat)

        print(boats)
        return len(boats)
    