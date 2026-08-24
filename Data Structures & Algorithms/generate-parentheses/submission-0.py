class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        ## brute force appoarch
        def isValid(s: str):
            balance = 0 
            
            for i in s:
                if i == "(":
                    balance += 1
                else: 
                    balance -= 1
                if balance < 0:
                    return False 
            
                ## if open is 0 return true same as return not balance
            if balance == 0:
                return True
            else:
                return False
                            


        def dfs(s: str):

            if len(s) == 2*n:
                if isValid(s):
                    res.append(s)
                return

            dfs(s + "(")
            dfs(s + ")")
        
        dfs("")
        return res