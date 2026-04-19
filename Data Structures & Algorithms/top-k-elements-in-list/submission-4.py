class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        res = []

        for num in nums:
            seen[num] = 1 + seen.get(num, 0)

        return sorted(seen, key=seen.get, reverse=True)[:k]