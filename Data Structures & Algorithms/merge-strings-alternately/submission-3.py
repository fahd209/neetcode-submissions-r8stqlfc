class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i = 0
        # j = 0
        res = ""

        while i < len(word1) and i < len(word2):
            res += word1[i]
            res += word2[i]

            i += 1
            # j += 1

        # if i < len(word1):
        #     for c in word1[i:]:
        #         res.append(c)

        # if i < len(word2):
        #     for c in word2[i:]:
        #         res.append(c)

        return res + word1[i:] + word2[i:]