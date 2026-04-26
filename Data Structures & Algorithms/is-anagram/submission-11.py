class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        word = {}

        for c in s:
            word[c] = word.get(c, 0) + 1

        for c in t:
            if c in word:
                word[c] -= 1
            else:
                return False

            if word[c] < 0:
                return False

        return True