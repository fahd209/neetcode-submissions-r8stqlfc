import re
class Solution:
    def isPalindrome(self, s: str) -> bool:

        # remove all the spaces
        s = s.replace(" ", "")

        def is_alphanumeric(c):
            return ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9') or ord('A') <= ord(c) <= ord('Z')
            

        # two pointers to check the left and right
        L = 0
        R = len(s) - 1

        while L < R:
            while L < R and not is_alphanumeric(s[L]):
                L += 1
            
            while R > L and not is_alphanumeric(s[R]):
                R -= 1

            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1


        return True
        
        