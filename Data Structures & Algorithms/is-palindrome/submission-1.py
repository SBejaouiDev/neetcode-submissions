import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip().translate(s.maketrans("","",string.punctuation))
        s= s.replace(" ", "")
        l = 0
        r = len(s) - 1
        print(s)

        while l <= r:
            print(f"comparing {s[l]} and {s[r]}")
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True


