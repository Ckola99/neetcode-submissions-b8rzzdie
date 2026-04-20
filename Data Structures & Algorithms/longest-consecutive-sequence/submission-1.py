class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sortedNums = sorted(set(nums))
        longest = 1
        current = 1

        for i in range(1, len(sortedNums)):
            if sortedNums[i] == sortedNums[i - 1] + 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 1

        return max(longest, current)