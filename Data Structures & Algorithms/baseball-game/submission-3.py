class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        Given a list of operations. 
        X: integer records new score
        +: records score that is previous of two scores
        D: record a new score that is double of the prev score
        C: invalidate the prev score, removing it from the rec

        P: Iterate through all the operations,
            if + add the two prevous scores
            if D stack[-1] and double it
            if c pop from the top of stack
            if its not one of those operations then it has to be an append

            
            Compute running total as we process operations instead of sum at the end.
           
        """
        res = [] 
        totalSum = 0

        for i in operations:
            # if i.isdigit() or i.lstrip('-').isdigit() :
            #     res.append(int(i))
            if i == "+":
                totalSum += int(res[-1]) + int(res[-2])
                res.append(int(res[-1]) + int(res[-2])) 
                print(totalSum)
            elif i == "D":
                totalSum += (2 * res[-1])
                res.append((res[-1] * 2))
                print(totalSum)
            elif i == "C":
                totalSum -= res[-1]
                res.pop()
                
            else: 
                totalSum += int(i)
                res.append(int(i))

        print("TS",totalSum)
        print(sum(res))
        return totalSum        
