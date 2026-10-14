
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        given a array strings

        an 2d array with each anagram in a array

        time: o(m * n)
        space: o(n)
        """
        anagrams_map = defaultdict(list)
        # find anagrams
        for s in strs:
            ord_arr = [0] * 26
            for c in s:
                ord_arr[ord(c) - ord('a')] += 1
            # print(ord_arr)
            anagrams_map[tuple(ord_arr)].append(s)
        

        return list(anagrams_map.values())