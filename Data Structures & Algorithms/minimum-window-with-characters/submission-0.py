class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        neededChars, currentWindow = {}, {}

        for c in t:
            neededChars[c] = neededChars.get(c, 0) + 1

        l = 0
        have, need = 0, len(neededChars)
        res, resLen = [-1,-1], float("infinity")

        for r in range(len(s)):
            cc = s[r]
            currentWindow[cc] = currentWindow.get(cc, 0) + 1

            if cc in neededChars and currentWindow[cc] == neededChars[cc]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                currentWindow[s[l]] -= 1
                if s[l] in neededChars and currentWindow[s[l]] < neededChars[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r + 1] if resLen != float("infinity") else ""
