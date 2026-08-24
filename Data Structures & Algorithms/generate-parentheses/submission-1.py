class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        """
        Understand. generate valid paraenthesis given an interger n representing pairs

        Plan: 
            brute force apporach generates all combinations of pairs. We use a dfs to choice two decisions open or close.
            When the length of the string is equal to 2 * n we check if the string is valid. 
            - if valid we append the solution.

            - to check if a string is valid. we keep a balance count. If "(" we increment balance by one else decrement. 
              if at any time balance is less than zero return false. Other wise if the balance is 0 we return True


        """
   
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