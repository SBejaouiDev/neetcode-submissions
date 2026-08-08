class Solution:
    def decodeString(self, s: str) -> str:
        """
        Given an encoded string. Decode the string. Given the format k[string]
        K represents how many times the string repeats 
        Ex: 2[a3[b]]c 2:A 3:B 1:C 
        2: repeat [a3 [b] ]c 
        decode [a 3[b] ] 
        3[b] = bbb
    
        """
        #closeToOpen  = {"]":"["}

        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else: 
                substr = ""
                # Pop characters until [ is found to build the substring.
                while stack[-1] != "[":
                    substr = stack.pop() + substr 
                stack.pop()
                print("substr",substr)

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                print("k:" ,k)
                repeatedSubstring = substr * int(k) 
                stack.append(repeatedSubstring)


        
        return "".join(stack)