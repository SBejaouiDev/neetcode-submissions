import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #pre-processing
        #s = s.lower()


        #left and right pointer
        l = 0
        r = len(s) - 1

        print(s)

        while l < r:

            while l < r and not self.alphaNum(s[l]):
                l += 1 
                
            while r > l and not self.alphaNum(s[r]):
                r -= 1


            print(l, r)
            print(f"comparing {s[l]} and {s[r]}")

            if s[l].lower() != s[r].lower():
                    return False

            l += 1
            r -= 1

        return True


    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

