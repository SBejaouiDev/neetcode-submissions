class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Understand 

        given a string made of digits from 2 - 9 return all possible letter combinations that digits could represent
        - Each digit is mapped to a set of characters
        - a digit could represent any one of the characters it maps to

        Plan 
        use backtracking algorithm. 
            - each level equals one digit 
            - each branch equals one possible character for that digit

        at index i pick one character from the mapping of digits[i]
        move to the next digit 
        once the len of the built string equals the number of digits, we have formed a valid combination

        if input string is empty return []

        use a recursive function(index, currentString)
            - if the len(currentString) = len(digitst) add it to the result and return **basecase
            - otherwise for each character mapped from digits[index] append the char to the
              current string and recursive to the next index

        """
        res = []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index,currentString):
            
            if len(currentString) == len(digits):
                res.append(currentString)
                return

            for char in digitToChar[digits[index]]:
                print(char,currentString)
                backtrack(index + 1,currentString + char)

            #reaching the botton is equivalent to return NONE 
        if digits:
            backtrack(0,"")

        return res

