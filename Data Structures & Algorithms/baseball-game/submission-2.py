class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        Given a list of operations. 
        X: integer records new score
        +: records score that is previous of two scores
        D: record a new score that is double of the prev score
        C: invalidate the prev score, removing it from the rec

        P: Iterate through all the operations,
            if integer append to stack, 
            if + add the two prevous scores
            if D stack[-1] and double it
            if c pop from the top of stack

        """
        res = [] 
        totalSum = 0

        for i in operations:
            print(res,totalSum)
            if i.isdigit() or i.lstrip('-').isdigit() :
                res.append(int(i))
            elif i == "+":
                print("+")
                totalSum += int(res[-1]) + int(res[-2])
                res.append(int(res[-1]) + int(res[-2]) ) 
            elif i == "D":
                print("D")
                res.append((res[-1] * 2))
                totalSum += res[-1]
                print(totalSum,res)
            elif i == "C":
                print("C", totalSum)
                res.pop()
        
        print(sum(res))
        print(res,totalSum)
        return sum(res)        
