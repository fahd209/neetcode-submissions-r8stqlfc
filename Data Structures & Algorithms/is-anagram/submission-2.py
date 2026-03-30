class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the string don't have the same length then they are not anagrams
        # use character counts(hashmaps) for both string
        # if the both hashmap contain the same character counts then return true else return false

        sCount = {}
        tCount = {}

        if len(s) != len(t):
            return False

        for c in s:
            sCount[c] = sCount.get(c, 0) + 1

        for c in t:
            tCount[c] = tCount.get(c, 0) + 1 

        return sCount == tCount

    
        