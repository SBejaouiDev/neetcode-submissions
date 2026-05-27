class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

                #strs = ["act", "pots", "tops", "cat", "stop", "hat"]

        res = defaultdict(list)
        for s in strs:
            ## Concatenates these characters without any seperator
            sortedS = "".join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())