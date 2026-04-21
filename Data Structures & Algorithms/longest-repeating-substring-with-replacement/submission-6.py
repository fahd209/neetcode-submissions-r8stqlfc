class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        right = 0
        charCount = {}
        longest_string_length = 0
        most_repeating_char = s[0]
        most_repeating_char_len = 1

        while right < len(s):
            c = s[right]
            charCount[c] = charCount.get(s[right], 0) + 1
            most_repeating_char_len = max(charCount[c], most_repeating_char_len)
            
            
            print(most_repeating_char_len)
            while ((right - left + 1) - most_repeating_char_len) > k and left < right: 
                charCount[s[left]] -= 1
                left += 1

                if charCount[s[left]] > most_repeating_char_len:
                    most_repeating_char_len = charCount[s[left]]
                
            
            longest_string_length = max(longest_string_length, (right - left))
            right += 1

            

        return longest_string_length + 1