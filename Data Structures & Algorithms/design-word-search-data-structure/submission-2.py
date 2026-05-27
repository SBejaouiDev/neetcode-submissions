import random

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self): ## self means the object created when we run for example wd = WordDictionary()
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        curr = self.root

        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            ##set curr to postion of 
            curr = curr.children[i]
                
        curr.endOfWord = True 


    def search(self, word: str) -> bool:
        #day
        #bay
        #may
        # searching for .ay

        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c = word[i]
        
                if c == ".":
                    for child in curr.children.values(): # try all nodes stored in the dictionary. d then b then m 
                        if dfs(i + 1, child): # continue to next character since we handled the ".". Inside recursive call j = 1 curr = d_node
                                              # Inside recursive call j = 1 curr= d_node c = "a" 
                                              # inside the else statement: check if a in children. a is so curr becomes a_node
                                              # next iteration c becomes "y". y is in children. curr becomes y_node
                                              # return the curr.endOFword which results in True
                                            
                            return True
                    return False


                else: 
                    if c not in curr.children: ## if c is not in curr.children
                        return False
                    curr = curr.children[c]

            return curr.endOfWord


        return dfs(0,self.root)
                
