class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        digits = {}

        for num in nums:
            digits[num] = 1 + digits.get(num, 0)

        return sorted(digits, key = digits.get, reverse=True)[:k]