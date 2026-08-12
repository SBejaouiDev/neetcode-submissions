class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """ 
        Use two pointers and alternate between the two strings, appending to a new string

        """

        s1 = 0 
        s2 = 0
        newString = ""

        while s1 < len(word1) or s2 < len(word2):
            if s1 >= len(word1):
                newString += word2[s2:]
                break
            elif s2 >= len(word2):
                newString += word1[s1:]
                break

            newString += word1[s1] + word2[s2]
            s1 += 1
            s2 += 1

        return newString
            