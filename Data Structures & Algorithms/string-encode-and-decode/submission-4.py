from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""

        for i in range(len(strs)):
            st += f"{len(strs[i])}#{strs[i]}"

        print("printing the string", st)
        return st


    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        print(s[0:2])

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j]) ## array slicing "5"
            i = j + 1
            j = i + length

            output.append(s[i:j])
            i = j

        return output

