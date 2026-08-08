class Solution:
    def decodeString(self, s: str) -> str:
        """
        Given an encoded string. Decode the string. Given the format k[string]
        K represents how many times the string repeats 
        Ex: 2[a3[b]]c 2:A 3:B 1:C 
        2: repeat [a3 [b] ]c 
        decode [a 3[b] ] 
        3[b] = bbb
        
        Plan: We use a stack and append all characters until we reach a closing bracket.
        once we reach a closing bracket we pop all the characters and append it to a substr until an opening
        bracket is found. 

        we then pop all digits and that result is our k which represents how many times to repeat our sustring
        we multiple our substring by k and append it to the stack. 

        Once we have processed the whole string we join the elements in the stack. 
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
                # pop [ from stack
                stack.pop()
                print("substr",substr)

                # pop all consecutive intgers to from the repeat count K
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                # repeat the substring k times and push result back onto the stack
                repeatedSubstring = substr * int(k) 
                stack.append(repeatedSubstring)


        
        return "".join(stack)