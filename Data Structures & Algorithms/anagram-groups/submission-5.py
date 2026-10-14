class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        given a array strings

        an 2d array with each anagram in a array
        """
        result = []
        anagrams_map = {}
        # find anagrams
        for s in strs:
            ord_arr = [0] * 26
            for c in s:
                ord_arr[ord(c) - ord('a')] += 1
            # print(ord_arr)
            anagrams_map[tuple(ord_arr)] = anagrams_map.get(tuple(ord_arr),[]) + [s]
        

        return list(anagrams_map.values())