class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ## tabulation bottom up


        ## memorization top down

        res = []
        part = []
        """
        Given a string split s into substrings where every substring is a palidrome. ABBA == ABBA, ABA == ABA 


        """

        def isValid(s:str,l,r):
            #print("Testing",s[l:r])
            while l < r:          
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        

        def dfs(j,i):
           # print(part,j,i)
            ## base case 
            if i >= len(s):
                #confused here 
                if i == j: 
                    #print("\n")
                    res.append(part.copy())
                return

            if isValid(s,j,i):
                part.append(s[j : i + 1])
                dfs(i + 1, i + 1)
                part.pop()

            dfs(j, i + 1)

        #print(isValid(s,0,0),"\n")
        dfs(0,0)
        
        return res