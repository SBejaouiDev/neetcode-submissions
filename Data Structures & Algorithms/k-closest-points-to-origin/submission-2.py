class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heapq.heapify(points)

        newHeap = [] # Ensure this is an empty list
        output = []

        while points: 
            coor = heapq.heappop(points)
            #print(coor, end = " " )
            # Euclidean distance 
            distance = (math.sqrt(math.pow((0 - coor[0]),2) + math.pow((0 - coor[1]),2)))
            heapq.heappush(newHeap,(distance,coor))


        output = []


        while k > 0:
            priority, second_element = heapq.heappop(newHeap)
            output.append(second_element)
            k -=1

        return output
