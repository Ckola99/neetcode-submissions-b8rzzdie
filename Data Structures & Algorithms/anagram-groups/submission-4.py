class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}
        for word in strs:
            key = "".join(sorted(word))

            if "".join(sorted(word)) == key:
                word_dict.setdefault(key, []).append(word)

        return list(word_dict.values())
                
