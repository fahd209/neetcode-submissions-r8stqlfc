class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # [0  0  0]
        #  0, 1, 2

        if len(s) != len(t):
            return False
        
        char_count = [0] * 26
        for i in range(len(s)):
            char_count[ord(s[i]) - ord('a')] += 1
            char_count[ord(t[i]) - ord('a')] -= 1 

        for n in char_count:
            if n != 0:
                return False
        return True

        