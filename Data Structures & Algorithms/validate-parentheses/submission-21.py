class Solution:
    def isValid(self, s: str) -> bool:
        """
        Given a string, check if it contains valid parentheses
        valid if
        - every open bracket closed by same type of closing bracket
        - open brackets are closed in the correct order 
        - every close bracket has a coressponding open bracket of the same type

        Examples: 
        - [] true

        - ({[]}) True

        - [(]) False open brackets are not closed in correct order
            correct format: [()]

        Plan: Stack to store characters. 
        - if its an open bracket push it onto stack. 
        - If the bracket is closing check the corresponding open bracket at the 
            top of the stack. If there is not a match we return false

        Im my first item i did a openToClose dictionary, the problem with this is that, we need to 
        match the corresponding elements in the stack. The stack contains open brackets. 
        it makes more sense to do closeToOpen, due to the nature of the stack. we can search the dictionary for the correct 
        opening brackets for each closing bracket. 
        dic[}] = { 
        stack[-1] = {
        that would formulate a match. 

        The reason to switch the if and else is because the dic is switched from closeToOpen. The dic contains closeToOpen
        keys. Check if its a closed first if not we append the opening bracket

        stack: ([{
        """
        #dic = {"(": ")", "{": "}" , "[": "]"}
        dic = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []
        for i in s:
            print(stack)
            if i in dic: 
                if stack and stack[-1] == dic[i] :
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False 