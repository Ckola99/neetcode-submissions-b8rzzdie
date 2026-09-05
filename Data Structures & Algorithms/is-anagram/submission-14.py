class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first the strings need to be same length
        if len(s) != len(t):
            return False

        seen = {}

        for c in s:
            seen[c] = 1 + seen.get(c, 0)
        
        for c in t:
            if c in seen:
                seen[c] -= 1
            else:
                return False

            if seen[c] < 0:
                return False
        return True