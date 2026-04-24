class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """

        approach:
            1. charCount for s1 -> dict
            2. loop over s2
            3. if a char is in the hashmap start a window
            4. track the window in another hashmap

        """

        if len(s2) < len(s1):
            return False

        charCount = {}

        # building initial hashmap
        for c in s1:
            charCount[c] = charCount.get(c, 0) + 1

        # loop over the s2 to look for a window that has the same characters as charCount
        for i in range(len(s2)):
            j = i
            current_char_count = {}

            while j < len(s2) and s2[j] in charCount:
                if s2[j] in current_char_count and current_char_count[s2[j]] >= charCount[s2[j]]:
                    break
                current_char_count[s2[j]] = current_char_count.get(s2[j], 0) + 1
                if current_char_count == charCount:
                    return True
                j += 1

        return False
        