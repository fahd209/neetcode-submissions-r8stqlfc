class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramsList = []
        angramsMap = {}

        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord in angramsMap:
                angramsMap[sortedWord].append(word)
            else:
                angramsMap[sortedWord] = [word]
            
        return list(angramsMap.values())