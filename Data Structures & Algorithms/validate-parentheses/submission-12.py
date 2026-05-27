class Solution:
    def isValid(self, s: str) -> bool:
        count = {"{": "}", "(": ")", "[":"]"}
        popList = []
        endList = []
        # if the next element is not the closing element in the dictionary
        ## the last elemt needs to be equal to its closing element
        if len(s) % 2 != 0:
            return False





        for i in range(len(s)):
            #print("Current element", [s[i]])

            if len(popList) == 0 and  s[i] not in count.keys():
                print("FIrst element did not start with opening bracket")
                return False

            if s[i] in count.keys():
                print(s[i])
                popList.append(s[i])
            
            if s[i] not in count.keys():
                if count[popList.pop()] != s[i]:
                    print("not in correct order")
                    return False
                print(s[i])
                endList.append(s[i])
    
    
    
            # #Input3 = "[(])"
            # if s[i] in count.keys():
            #     print(s[i])
            #    # print("appending this " ,count[s[i]])
            #     popList.append(count[s[i]])
            #     #print("After appending", popList)
            #
            # ## end list
            # if s[i] in count.keys():
            #     endList.append(count[s[i]])

        ## WILL BE USING THIS TO CHECK
        # for i in endList:
        #     if endList.pop() != popList.pop():
        #         return False

        if len(endList) == 0 or len(endList) and len(popList):
            return False 

        print(len(endList))
        print("endList", endList)
        print("PopList", popList)


        return True






