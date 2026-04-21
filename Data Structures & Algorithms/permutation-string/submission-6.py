class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create two variables to store hashmaps

        s1_char_count = {}
        s2_window_char_count = {}

        # seed the hashmaps
        for char in s1:
            s1_char_count[char] = 1 + s1_char_count.get(char, 0)

        for char in s2[:len(s1)]:
            s2_window_char_count[char] = 1 + s2_window_char_count.get(char, 0)

        if s1_char_count == s2_window_char_count:
            return True

        for i in range(len(s1), len(s2)):
            incoming_char = s2[i]
            outgoing_char = s2[i - len(s1)]

            s2_window_char_count[incoming_char] = s2_window_char_count.get(incoming_char, 0) + 1

            s2_window_char_count[outgoing_char] -= 1
            if s2_window_char_count[outgoing_char] == 0:
                del s2_window_char_count[outgoing_char]
                
            if s1_char_count == s2_window_char_count:
                return True

        return False