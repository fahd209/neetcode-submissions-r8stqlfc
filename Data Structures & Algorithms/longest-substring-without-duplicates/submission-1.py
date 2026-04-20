class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0
        window_characters = set()
        i = 0

        for j in range(len(s)):
            while s[j] in window_characters:
                window_characters.remove(s[i])
                i += 1

            window_characters.add(s[j])
            max_length = max((j - i) + 1, max_length)
            

        return max_length