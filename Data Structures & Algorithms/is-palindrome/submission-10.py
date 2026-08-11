class Solution:
    def isPalindrome(self, s: str) -> bool:


        """
        Use two pointers to iterate and compare the left side from the right side. 

        Left and right pointer. 

        **This is to skip spaces and punctuation**
            while l < r and current char is not alpha. 
            - increment l by 1
            while r < l and current char is not alpha
            - decrement r by 1

        We then compare if the left and right are the same.
            - return false when the cases dont match.
        
        increment left and right pointer

        If it iterates through the whole string return True

    
        """
        l = 0 
        r = len(s) - 1 
        #cleaned_text = "".join(char for char in text if char.isalnum())
        
        while l < r: 

            while l < r and not s[l].isalnum():
                l += 1 

            while r > l and not s[r].isalnum():
                r -= 1

            if s[r].lower() != s[l].lower():
                return False

            l += 1 
            r -= 1

        return True