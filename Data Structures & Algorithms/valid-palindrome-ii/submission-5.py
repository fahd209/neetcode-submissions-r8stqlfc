class Solution:
    def validPalindrome(self, s: str) -> bool:

        L = 0
        R = len(s) - 1

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1
            return True

        while L < R:
            if s[L] != s[R]:
                return isPalindrome(L + 1, R) or isPalindrome(L, R - 1)

            L += 1
            R -= 1


        return True



        # 30/31        
        # L = 0
        # R = len(s) - 1
        # nums_removed = 0

        # while L <= R: 

        #     if s[L] != s[R]:

        #         if s[L + 1] == s[R]:
        #             L += 2
        #             R -= 1
        #             nums_removed += 1
        #             if nums_removed > 1:
        #                 return False
        #             continue

        #         if s[R - 1] == s[L]:
        #             R -= 2
        #             L += 1
        #             nums_removed += 1
        #             if nums_removed > 1:
        #                 return False
        #             continue

        #         return False
        #     else:
        #         L += 1
        #         R -= 1

        # return True