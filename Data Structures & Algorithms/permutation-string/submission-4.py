class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1count = {}
        windowcount = {}

        for char in s1:
            s1count[char] = s1count.get(char, 0) + 1

        for char in s2[:len(s1)]:           # seed the first window
            windowcount[char] = windowcount.get(char, 0) + 1

        if s1count == windowcount:
            return True

        for i in range(len(s1), len(s2)):   # slide one character at a time
            incoming = s2[i]
            outgoing = s2[i - len(s1)]

            windowcount[incoming] = windowcount.get(incoming, 0) + 1

            windowcount[outgoing] -= 1
            if windowcount[outgoing] == 0:
                del windowcount[outgoing]   # keep maps clean for == comparison

            if s1count == windowcount:
                return True

        return False

        

