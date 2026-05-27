class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
  
        if len(s) != len(t):
            return False

        freqS = {}
        freqT = {}

        for char in s:
            freqS[char] = freqS.get(char, 0) + 1

        print(freqS)

        for char in t:
            freqT[char] = freqT.get(char, 0) + 1

        print(freqT)

        if freqS.keys() != freqT.keys():
            return False


        for i in freqS:
            if freqS.get(i) == freqT[i]:
                continue
            else:
                return False

        return True 

        