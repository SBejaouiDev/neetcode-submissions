class Solution:
    def validPalindrome(self, s: str) -> bool:

        """ 
        Two pointers

        Check the left and right, if the strings do not match, replace a single chacacter.
        Replace character by slicing the string into two arrays skipL and skipR.
        - skipL moves to the left by one character
        - skipR moves to the right by one character

        Check to see if either of the new strings with the character removed is a valid Paindrome
        - check sliced array with the reverse of itself for left and right. If one matches return True

        otherwise

        """
        l = 0 
        r = len(s) - 1 
        #cleaned_text = "".join(char for char in text if char.isalnum())
     
        while l < r: 


            if s[l] != s[r]:

                #Skip the left and right char 
                skipL = s[l + 1 : r + 1]
                skipR = s[l : r]

                print(skipR,skipR[::-1])
                print(skipL,skipL[::-1],)
                
                #reverse the newString with the skipped element and compare it to see if its a palinedrome
                return skipL == skipL[::-1] or skipR == skipR[::-1]

            l += 1 
            r -= 1 

 

        return True