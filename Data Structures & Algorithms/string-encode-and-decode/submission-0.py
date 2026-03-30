class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += s + '|'
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        j = 0
        decoded = []
        while i < len(s):
            if s[i] == '|':
                word = s[j:i]
                decoded.append(word)
                j = i + 1
            i += 1
        return decoded


        