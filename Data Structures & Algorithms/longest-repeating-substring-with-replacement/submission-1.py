class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # I want to create a hashmap of the characters in the string to get their count
        count = {}

        # need a variable to count the longest string
        longest = 0
        
        l = 0
        # lets iterate through the string
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) # store the count of the character eg {A: 1}

            # now we check if the string is valid for the change of k against the available characters
            while (r - l + 1) - max(count.values()) > k:
                
                # we want to decrement the characters count that was removed
                count[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest